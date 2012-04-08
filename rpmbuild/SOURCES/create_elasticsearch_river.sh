#!/bin/bash

HOST=${1:-"localhost"}
PORT=${2:-"9200"}

echo "Using host=${HOST} port=${PORT}"

# check to see if elasticsearch already has the river created
check_river() {
    COUNT=$(curl -XGET "${HOST}:${PORT}/_river/my_river/_meta" -s|grep elasticsearch|wc -l)
    RESULT=$?
    echo result=${RESULT}
    if [ $RESULT != 0 ]; then
        echo "Problem getting river information from elasticsearch"
        exit 1;
    fi
    echo count=${COUNT}
    if [ $COUNT == 3 ]; then
        echo "Found existing elasticsearch river"
        exit 0
    else
        echo "Elasticsearch river not found"
    fi
}

check_river
echo "Creating elasticsearch river"

# create the river - this is straight from the elasticsearch rabbitmq river doc
curl -XPUT "${HOST}:${PORT}/_river/my_river/_meta" -d '{
    "type" : "rabbitmq",
    "rabbitmq" : {
        "host" : "localhost", 
        "port" : 5672,
        "user" : "guest",
        "pass" : "guest",
        "vhost" : "/",
        "queue" : "elasticsearch",
        "exchange" : "elasticsearch",
        "routing_key" : "elasticsearch",
        "exchange_type" : "direct",
        "exchange_durable" : true,
        "queue_durable" : true,
        "queue_auto_delete" : false
    },
    "index" : {
        "bulk_size" : 100,
        "bulk_timeout" : "10ms",
        "ordered" : false
    }
}'

check_river

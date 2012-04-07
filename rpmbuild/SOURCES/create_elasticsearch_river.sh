#!/bin/bash

# this is straight from the elasticsearch rabbitmq river doc
curl -XPUT 'localhost:9200/_river/my_river/_meta' -d '{
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

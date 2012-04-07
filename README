This is a collection of builds for recent versions of the following libraries
to get log processing with logstash/elasticsearch up and running over AMQP.

* logstash - parse logs and send them to elasticsearch
* grok - logstash dep
* elasticsearch - store and index the logs
* elasticsearch-plugin-river-rabbitmq - amqp listener for elastisearch
* kibana - web front-end for elasticsearch

I had to track down correct versions of libs, patch one of them, add some extra
resources and get everything into packages for both CentOS 5 & 6.  Hopefully
these will help someone for now, until updated/tweaked packages from more
official sources can be easily obtained.

Please see all respective SPEC files for information on licensing of those
modules and their sources.  More information can be found at the official
websites for each module.  Apache Ant is bundled for the logstash build and is
distributed under the Apache license...shocking, I know.

When building, you may want to use the .rpmmacros file by placing it in your
user home directory of your build box.  This will easily allow you to build as
a non-root user.  Copy files out of this project structure into your existing
rpmbuild directory, or simply "ln -s log-processing/rpmbuild" into your user
home directory.

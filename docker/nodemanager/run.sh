#!/bin/bash

./entrypoint.sh

$HADOOP_HOME/bin/yarn --config $HADOOP_CONF_DIR nodemanager

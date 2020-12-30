#!/bin/bash
set -e

sleep 2

flask db upgrade

if [ $OTELE_TRACE = "True" ]
then
    echo "Running with OpenTelemetry"
    opentelemetry-instrument -e none flask run --host=0.0.0.0
else
    echo "OpenTelemetry isn't enable"
    flask run --host=0.0.0.0
fi
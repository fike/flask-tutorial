#!/bin/bash
set -e

sleep 2

flask db upgrade

flask run --host=0.0.0.0

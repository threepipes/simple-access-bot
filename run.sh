#!/bin/bash
DIR_NAME=`dirname $0`
source $DIR_NAME/.venv/bin/activate
export CHROMEDRIVER_PATH=/usr/bin/chromedriver
python $DIR_NAME/bot.py

#!/bin/bash

cd $APP_DIR

source $VIRTUAL_ENV/bin/activate

uvicorn server:app --port 3002 --host 0.0.0.0 --workers 5
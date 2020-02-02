#!/bin/bash

cd $APP_DIR && python -m venv venv
echo "venv created. "

echo "python --version"
python --version
which python

echo "python3 --version"
python3 --version
which python3

source ./venv/bin/activate && \
  echo "venv activated." && \
  pip install --upgrade pip && \
  echo "Upgraded pip." && \
  pip install -r requirements.txt

echo "Installed requirements"






#!/bin/bash

#python -m pip install --upgrade virtualenv
#python -m virtualenv venv
#./venv/bin/pip install -r requirements.txt

python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements.txt

#!/usr/bin/env bash

pip3 install virtualenv
virtualenv -p python3 django_venv
source django_venv/bin/activate
pip3 install -r requirement.txt


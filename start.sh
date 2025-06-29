#!/bin/bash

python manage.py migrate
python manage.py initial
python -m leonbot


#!/bin/bash
echo "creating Migrations.."
python manage.py makemigrations course
echo "============================="

echo "Starting Migrations.."
python manage.py migrate
echo "============================="

echo "generate dummy data"
python dummy_data.py
echo "============================"
echo "starting The server.."
python manage.py runserver 0.0.0.0:8000
echo "============================="


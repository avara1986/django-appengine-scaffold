#!/bin/bash
echo "Activando virtualenv..."
source 'vapp/bin/activate'
echo "Ejecutando servidor..."
python manage.py runserver
echo "Apagando virtualenv..."
deactivate

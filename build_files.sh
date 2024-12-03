#!/bin/bash
# build_files.sh
pip install -r requirements.txt
python3.9 manage.py collectstatic

echo "Aplicando migraciones..."
python3.9 manage.py makemigrations || { echo "Error al ejecutar makemigrations"; exit 1; }
python3.9 manage.py migrate || { echo "Error al ejecutar migrate"; exit 1; }

echo "Recolectando archivos estáticos..."
python3.9 manage.py collectstatic --noinput || { echo "Error al recolectar archivos estáticos"; exit 1; }

echo "Script ejecutado con éxito."

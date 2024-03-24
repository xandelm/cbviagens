#!/bin/bash

echo "Implemente aqui o script para executar a sua solução"
cd app
python -m venv .
.\Script\activate
#source Scripts/activate
pip install -r requirements.txt
cd cbviagens
python manage.py migrate
python manage.py load_data
python manage.py runserver 3000 &
cd ../cbviagens-front
yarn install
yarn add @quasar/cli
yarn quasar dev

#deactivate

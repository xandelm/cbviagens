#!/bin/bash

echo "Implemente aqui o script para executar a sua solução"
#.\Script\activate
cd cbviagens || exit
python -m venv .
source Scripts/activate
pip install Django
pip install -r requirements.txt
python manage.py migrate
python manage.py load_data
python manage.py runserver 3000 &
cd ../cbviagens-front || exit
yarn install
yarn add @quasar/cli
yarn quasar dev

#deactivate

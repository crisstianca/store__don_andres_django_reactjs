#!/user/bin/env bash

set -o errexit # exit on error

pip install -r requirements.txt

python manage.py collectstactic --no--input
python manage.py migrate

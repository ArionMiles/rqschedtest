# rqschedtest

## Setup

1. `git clone https://github.com/ArionMiles/rqschedtest`
2. Create a virtualenv and activate it
3. `pip install requirements.txt`
4. Edit `.env` with appropriate redis-server URL
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. `python manage.py runserver`
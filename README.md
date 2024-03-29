# rqschedtest

Repo for testing multiple RQ-Schedulers running in Fail-Over mode.

Link to relevant [Issue](https://github.com/rq/rq-scheduler/issues/195) and [PR](https://github.com/rq/rq-scheduler/pull/212) on rq-scheduler

## Setup

1. `git clone https://github.com/ArionMiles/rqschedtest`
2. Create a virtualenv and activate it
3. `pip install -r requirements.txt`
4. Edit `.env` with appropriate redis-server URL
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. `python manage.py runserver`

## Running

1. Start `redis-server` on port 6379 (default)
    - Or you can `docker-compose up` to launch a redis container
2. Start rqworker with: `python manage.py rqworker`
3. Start 2 or more rqschedulers with: 
    - `python3 manage.py rqscheduler -v 3 -i 10`
    - `python3 manage.py rqscheduler -v 3 -i 8`
    - `python3 manage.py rqscheduler -v 3 -i 5`
4. Schedule a job to run every minute using `python manage.py jobs`

**Notes:**

1. `localhost:8000/say-hello` will enqueue `say_hello` function to rqworker
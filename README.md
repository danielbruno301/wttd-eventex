# Eventex

[![Build Status](https://travis-ci.org/danielbruno301/wttd-eventex.svg?branch=master)](https://travis-ci.org/danielbruno301/wttd-eventex)
[![Code Health](https://landscape.io/github/danielbruno301/wttd-eventex/master/landscape.svg?style=flat)](https://landscape.io/github/danielbruno301/wttd-eventex/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/4996c69271b349e4a682/maintainability)](https://codeclimate.com/github/danielbruno301/wttd-eventex/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4996c69271b349e4a682/test_coverage)](https://codeclimate.com/github/danielbruno301/wttd-eventex/test_coverage)

This project aims to improve Python and Django skills applying TDD as development methodology

System for a Conference commissioned by a pseudo-client akka Morena.

Use libraries as:

dj-database-url | dj-static | python-decouple | gunicorn 


## How to develop

1. Clone the Repository.
2. Create a virtualenv with Python 3.6.3
3. Activate the virtualenv.
4. Install the dependencies.
5. Configure the instance with .env
6. Run the tests.

```console
git clone https://github.com/danielbruno301/wttd-eventex wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## How to deploy

1. Create an instance in heroku.
2. Send the settings to heroku.
3. Define a secure SECRET_KEY for the instance.
4. Set DEBUG=False
5. Configure the email service.
6. Send the code to heroku.

```console
heroku create myinstance
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#Configure your email
git push heroku master --force
```

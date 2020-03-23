## Delivery service with Flask

##### features:
 - main page for show random 3*5 meals by categories 
 - profile page for show orders detail and history
 - cart page for send new order
 - admin panel for manage delivery service
 
##### requirements:
 - Python 3.5+
 - Flask 1.1.1
 - Gunicorn 20.0.4

##### install requirements:
`pip3 install -r requirements.txt`

##### create and fill db:
`flask db upgrade`

`python fill_db.py`

##### run app:
 - run `gunicorn 'wsgi:app'`
 - open default page http://127.0.0.1:8000
 - use test user admin@localhost.com

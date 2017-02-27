# ClubManner

## Get Started

This assumes you have your PostgreSQL database running and are on MacOS.

1. Run the following command to install the required Python packages
    
    $ pip install -r requirements.txt

2. Create virtualenv with the following command

    $ virtualenv clubmannerenv

3. Activate the virtual environment by running the follwing command

    $ source clubmannerenv/bin/activate

3. Create the database `djangoadmin` in PostgreSQL and run the following command

    $ psql -U postgres -c "create role djangouser login password 'password'"

4. Make migrations, this should create/set up the database

    $ ./manage.py makemigrations
    $ ./manage.py migrate

5. Create an authorized user for yourself

    $ ./manage.py create superuser

6. Start the local server

    $ ./manage.py runserver

7. Navigate to `localhost:8000/product/get` and login at the top right and you should get an HTTP response code of 200. Or use something like [Postman](https://www.getpostman.com/) with the endpoint `localhost:8000/product/get` and with your user credentials in the authorization tab


## Requirements

+ Python 3.6
+ pip
+ PostgreSQL 9.4 or newer
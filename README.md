## Test Backend

## Technology Stack

   [Django framework 3.0.7](https://www.djangoproject.com/)

   [Django rest framework 3.11 - Build API Rest Ful](https://www.django-rest-framework.org/)

   [Postgres](https://www.postgresql.org/)

   [sqlite3](https://www.sqlite.org/)

# Install

Create virtual enviroment

    virtualenv -p python3 env

Clone the project and run the commands as show in the order inside the virtual enviroment.

### Note: Download .env - enviroment's variables

1. Install all the requirements

    `pip install -r requirements/development.txt`

2. Migrate the migrations

    `python manage.py migrate`

3. Create super user

    `python manage.py createsuperuser`

4. Run server

    `python manage.py runserver`


# API Documentation

[API Documentation](https://documenter.getpostman.com/view/11766693/T1LV7ibh)
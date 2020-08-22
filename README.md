## Test Backend

## Technology Stack

   [Django framework 3.0.7](https://www.djangoproject.com/)

   [Django rest framework 3.11 - Build API Rest Ful](https://www.django-rest-framework.org/)

   [Postgres](https://www.postgresql.org/)

   [sqlite3](https://www.sqlite.org/)

   [Docker - PostGIS Image for development](https://www.docker.com/)

# Install

Create virtual enviroment

    virtualenv -p python3 env

Clone the project and run the commands as show in the order inside the virtual enviroment.

# Install Dependencies for GEODjango

`sudo apt install gdal-bin libgdal-dev`
`sudo apt install python3-gdal`

### Note: Download .env - enviroment's variables

#### Install Docker

[Instructions for install docker](https://docs.docker.com/get-docker/)


1. [ Download PostGIS Image](https://hub.docker.com/r/kartoza/postgis/)

    `docker pull kartoza/postgis`

2. Run Image with docker
    `docker run --name "postgis" -p 25432:5432 -d -t kartoza/postgis`

3. Config variables PostGis

    ######   Note: Default postgresql user is 'docker' with password 'docker'.

    ##### This variables add to .env file.

    * NAMEDBPG
    * USERDBPG
    * PASSWORDDBPG
    * PORT


4. Install all the requirements

    `pip install -r requirements/development.txt`

5. Migrate the migrations

    `python manage.py migrate`

6. Create super user

    `python manage.py createsuperuser`

7. Run server

    `python manage.py runserver`


# API Documentation

[API Documentation](https://documenter.getpostman.com/view/11766693/T1LV7ibh)

## References
[Postgis](https://github.com/kartoza/docker-postgis)
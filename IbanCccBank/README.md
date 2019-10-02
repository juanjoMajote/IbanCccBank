  **IbanCccBank**
  = 

Application developed in django for the management of IBAN bank accounts numbers.
CRUD views have been implemented for reading, creating, updating and deleting clients.

**Local Implementation**
-

- ###**Requirements Installation.**
The requirements found in the requirements.txt file are installed. For this we execute

````bash
pip install -r requirements.txt
````

- ### **Configuration settings file.** ###
I have created a configuration file one to work with a bbdd ** Sqlite **. By default it is set
to work with a bbdd postgress.
To run the application with a ** Sqlite ** configuration file

````bash
python manage.py makemigrations --settings=IbanCccBank.settings_sqlite

python manage.py createsuperuser --settings=IbanCccBank.settings_sqlite
python manage.py runserver --settings=IbanCccBank.settings_sqlite
```` 
If you are going to work with postgress, you must enter the connection data to the bbdd:

````python
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2'
        'NAME': 'bbddibam', # nombre de la bbdd
        'USER': 'prueba', #usuario
        'PASSWORD': 'postgress', # password 
        'HOST': 'db_postgress', # ip o nombre de host
        'PORT': 5432 # puerto de conexión
    }
}
````

- ###**Creation and migrations of BBDD.**
Execute the following commands for the creation of the DBBD.

````bash
python manage.py makemigrations
````

````bash
python manage.py migrate
````
for Sqlite:

````bash
python manage.py makemigrations --settings=IbanCccBank.settings_sqlite
python manage.py migrate --settings=IbanCccBank.settings_sqlite

````
for create the superuser:
````bash
python manage.py createsuperuser
````
for Sqlite:
````bash
python manage.py createsuperuser --settings=IbanCccBank.settings_sqlite
````
To run the application you must launch the following command.

````bash
python manage.py runserver
```` 
for Sqlite:
````bash
python manage.py runserver --settings=IbanCccBank.settings_sqlite
````

**Implementacion con Docker**
-

- Docker Image Creation.
To create the docker image we launch the following command:
````bash
./create_image_django.sh
````
o
````bash
docker image build -t djangoiban:latest .
````
- Creation of application services.
For the creation of services we must follow the following steps:
   - We modify the file ** docker-compose prod.yml ** and modify the data of bbdd and the application.
 ````yaml
version: '3.3'
services:
    db_postgress:
      image: postgres:latest
      environment:
         - POSTGRES_USER=prueba   # user postgress
         - POSTGRES_PASSWORD=postgress  # pass
         - POSTGRES_DB=bbddibam # name bbdd
      volumes:
         - db-data1:/var/lib/postgresql/data
      networks:
         - dbs
    djangoiban:
      image: djangoiban:latest
      ports:
        - "8000:8000"
      networks:
        - dbs
      environment:
        - DJANGO_SUPER_USER=juanjo2 # superuser django
        - DJANGO_PASS=prueba   # pass
        - DJANGO_EMAIL=juanjo2.majote@gmail.com #email
      depends_on:
      - db_postgress

volumes:
  db-data1:

networks:
  dbs:
```` 
   - We create the services by executing the following command..
 
    
````bash
docker stack deploy -c docker-compose_prod.yml "nombre del servicio"
````

##Nota:
If the application does not work correctly the first time we start it, restart the django container so that it correctly 
applies the migrations and the creation of the superuser.

Configuring the Google Authentication API
=
To perform this task, we go to the 
[Google Developers Console](https://console.developers.google.com/) and, once there, we navigate to the Credentials 
section in the left menu. An select or create a project. Create o select  Web application and fill the required data.

The following [post](https://medium.com/trabe/oauth-authentication-in-django-with-social-auth-c67a002479c1) explains 
how to correctly configure the authentication using a google account.


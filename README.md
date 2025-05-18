# pabapp – Django Project

Welcome to pabapp budgeting tool built with Django.

**NOTE:** This project is WIP.

## Local development

To run this project in your development machine, follow these steps:

* Install dependencies:

    `pip install -r requirements.txt`

* Generate migration files:

    `python manage.py makemigrations`

* Apply migration files to database:

    `python manage.py migrate`

* For access to admin site, create a superuser:

    `python manage.py createsuperuser`

* If everything is alright, you should be able to start the Django development server:

    `python manage.py runserver`

* Open your browser and go to http://127.0.0.1:8000, you will be greeted with `Page not found (404)`, because there is no welcome page yet, but you can try to navigate to listed pages.

# django-admin startproject myproject
# cd myproject
# python manage.py runserver
# myapp/views.py


# What is Django 
"""Django is a high-level python web framework that enables rapid develpment
of secure and scalable web applications. It follows the Model-View_Architectue (MVC) and 
reusability, security, and scalability."""

# Why Use Django 
"""" 
    1. Fast Development 
    2. Security
    3. Scalability 
    4. Fully loaded it comes with built-in functionalities like authentication, databse ORM, form handling admin panel, etc
    5. Versatile 
"""

# Good practice to use a virtual enviroment for Dango projects.
# creating django project, use:
"""django-admin startproject progjectname

    myproject/
│── manage.py          # Command-line utility for Django
│── myproject/         # Main project directory
    │── __init__.py    # Treats this directory as a Python package
    │── settings.py    # Project settings
    │── urls.py        # URL configurations
    │── asgi.py        # ASGI entry point
    │── wsgi.py        # WSGI entry point
    
"""
#Running The Develpment Server
"""cd myprojectname
    python manage.py runserver."""

#Creating a Django App
"""python manage.py startapp myapp 

            myapp/
        │── migrations/       # Database migrations
        │── __init__.py       # Treats this directory as a package
        │── admin.py          # Configures the Django Admin
        │── apps.py           # App configuration
        │── models.py         # Defines database models
        │── views.py          # Handles application logic
        │── tests.py          # Contains tests
        │── urls.py           # Defines URL patterns for this app
"""
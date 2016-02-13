# FoodValleyBD

A Django based web project for searching desired food item at nearest location accross the country. Includes registration, food-item management, location integration service for restaurants and 
search service based on desired food-item, ingredient, location, budget for user in general.

## Platform
### Language
* Python 2.7
* HTML
* CSS
* JavaScript

### Database Management System
* MySQL

### Library & Framework
* jQuery
* Bootstrap
* Django 1.7
* MySQL-python
* django-admin-bootstrapped

### API / Service
* Google Map API (JavaScript v3)


## Setup
Applicable for Ubuntu or Ubuntu based distributions:
* Open terminal (```Ctrl + Alt + T```) and issue the following commands sequentially :
  * Install required packages :
    
    ```sudo apt-get install python-dev libmysqlclient-dev```
  * Install Virtualenv & Virtualenvwrapper :
    
    ```sudo pip install virtualenv virtualenvwrapper```
  * Create a new Virtualenv for the project and switch to that :  
    
    ```mkvirtualenv -p /usr/bin/python2.7 foodvalleybdenv```
    
    ```workon foodvalleybdenv```
  * Install Django and other required packages in created Virtualenv :
  
    ```pip install --upgrade pip```
    
    ```pip install django==1.7 django_admin_bootstrapped MySQL-python```
  
  * Create a database in MySQL database management system named ' **foodvalleybd** '  
  
  * Go to the project directory :
    ```cd FoodValleyBD``` (for example)
  * Issue the following commands :
    ```python manage.py makemigrations restaurant```

    ```python manage.py makemigrations search```

    ```python manage.py syncdb```
  * You will be asked to create a super user. Follow instructions to create an admin for the website.
  * Migrate & start the development server :
  
    ```python manage.py migrate```
    
    ```python manage.py runserver```
  * Browse http://127.0.0.1:8000/ from your browser.

## History
This Project was developed in between **December 2014** to **March 2015** as an academic project under the course " **Software Development Project - II** " taken by **Department of Computer Science & Engineering**, **Khulna University of Engineering and Technology**.

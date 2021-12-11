## AWARDS

# Author
Khalid Serar

# Description
This a Django Awards replica where a user can post a project together with the project's link, the projects can be viewed and aslo be rated according to the criteria given. The user can also click the link button to view what the project contains.

# Setup & installations
To get the code, clone the repository: https://github.com/khalid-serar/Awards-App.git and run the following commands;

$ cd Awards-app
$ pip install -r requirements.txt

# Install and actiavte the virtual environment
$ python3.8 -m venv virtual 
$ source virtual/bin/activate
# Create a database
$ psql
$ CREATE DATABASE (name_of_database);
# Make migrations
$ python3.8 manage.py check
$ python3.8 manage.py makemigrations (app_name)
$ python3.8 manage.py migrate 
# Testing the Application
$ python3.8 manage.py test (app_name)
# Running the Application
$ python3.8 manage.py runserver

Then once you are done, open your browser with the local host; 127.0.0.1:8000


# Technologies used
1.python 3.8.10
2.HTML
3.Django 3.2.5
4.Bootstrap 3
5.Heroku
6.Postgresql


# Dependencies
1.python3.8
2.Django 3.2.5
3.Virtual environment
4.Heroku
5.Gunicorn


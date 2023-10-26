"""
Python Flask Web App Boilerplate
====================

Description:
------------
A utility to simplify the initialization of Flask projects. The program asks the user for their project
name and then builds the boilerplate file structure.

Developer Information:
----------------------
Name: Telat Kaya

"""

import os
import shutil
from shutil import Error
from pathlib import Path
# Take user preference input
root_path = "./"

'''Function to create directories'''

def make_directory(path):
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)


'''Function to create files'''


def make_file(dir, name, cont, ext):
    n = name + ext
    try:
        with open(n, "w",encoding="utf8",) as file:
            file.writelines([cont])
            file.close()
            try:
                shutil.move(n, dir)
                print("File %s moved to %s" % (n, dir))
            except FileNotFoundError as err:
                print("File %s already exists in %s" % (n, dir))
            print("File %s%s created successfully!" % (name, ext))
    except FileExistsError:
        print("File %s%s already exists" % (name, ext))


# Create Folder Structure
make_directory(root_path + "/templates")
make_directory(root_path + "/static")
make_directory(root_path + "/static/images")
make_directory(root_path + "/tests")

# Data for files
layout = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="/static/style.css" rel="stylesheet" type="text/css" />
    <title>{% block title%}{% endblock%}</title>
  </head>
  <body>
    {% block content %} {% endblock %}
  </body>
</html>
'''
index = '''{% extends 'layout.html' %} {% block title %} Home Page {%
endblock %} {% block content %}
<h1>Hello World</h1>
{% endblock %}'''
style = " "
app = '''from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')'''
readme = '''# Introduction'''

# Create Files
make_file("", "app", app, ".py")
make_file("", "readme", readme, ".md")
make_file("templates", "layout", layout, ".html")
make_file("templates", "index", index, ".html")
make_file("static", "style", style, ".css")

# Install Dependencies and Start Flask
def install():
    os.system('python -m venv venv')
    os.system(r'venv\Scripts\activate')
    os.system('pip install flask')
    os.system('flask run')

install()

# Closing message
print("Have fun!")

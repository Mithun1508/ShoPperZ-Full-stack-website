# Created a My Basic Full-Stack Web site with Vue and Flask

# Introduction

This project is about a Single Page Application, SPAs usually are written using javascript, in this case, 
we used a Javascript Framework called Vue.js, and the frontend depends on a backend written in Python, 
this backend is offering only the basic login features, register, login, and logout. The data is saved into a Microsoft SQL Server database.

# Technologies used 

# Backend: 
Python, Flask, SQLAlchemy, virtualenv

# Frontend: 
Javascript, Vue.js, Vuetify, Axios

# Database: 
 Microsoft SQL Server

Dependencies in this project we will use some third-party libraries, for our luck Python comes with a package manager, that download and install the libraries for us, so let’s install them, execute one command by line:

pip install blinker

pip install cryptography

pip install Flask

pip install Flask-Login

pip install Flask-SQLAlchemy

pip install PyJWT

pip install pyodbc

pip install SQLAlchemy

pip install Werkzeug

# Service class 

To deal with some subjects let’s use some classes, it’s a good practice to use classes and methods specialized in one subject.
On the root folder of the project create a new folder called services

# Models
We gonna need some model files to exchange data between our methods.

# Main File
Every computer program has a start point, 
so in Python is not different, our entry point will begin  create a new file called main.py

# Data structure creator 
To create the database tables you can use this script, create a new file on the backend root folder


# Front-End using Vue.js
To use Vue js we first need to set up our machine with some prerequisites:
Node js: go to https://nodejs.org/ and follow the instructions to install it on your platform, please set the node into the path so you can use node from windows command prompt.
NPM (Node package manager): if you are using windows it will install by default along with Node js.
Vue js client: to install it, open a new command window and type:
npm install -g @vue/cli
Or access https://cli.vuejs.org/guide/installation.html and follow the instructions.

Vue js client is a wizard which help us to create a new Vue app, this application will run apart from our python backend, 
we will start to use Javascript programming language to write this frontend application.


# Vue Router
Simple page applications (SPAs) like this one uses a router to be able to navigate between views Vue.js provides us a built-in router. Once it is selected the Vue Client installer will configure it for us, so we need just to add new routes on it.

# Vuex as a State Management
It’s a state management library, it allows us to organize the data into our frontend, 
it will provide us a single source of data so all data manipulation will be placed in one place, instead of many files.

After executing the yarn serve, try to access http://localhost:8080/ a page must load with a default Vue app

The last dependency of our frontend is the Axios.js please install it using this command:

npm install axios --save

Navbar

A Vue component is divided into three parts,

Template: this defines with HTML this component will render, it could be written using HTML or other components, in the case above we used some components, for instance, v-app-bar

Script: in this section we set the logic of the component when we need to implement an action when the user clicks on a button, checks some data, retrieves some data from the server and etc, this is the part that will deal with the computation of the component.

Style (optional): this section will be used when you want to customize some CSS style for this particular component, so all CSS should be placed here.
Create a new file inside the components folder, name it Navbar.vue and paste this content in it:

My website looks like this 

![Screenshot (50)](https://user-images.githubusercontent.com/93249038/213121240-2c32139a-9b45-4f5a-9579-ea13e56cbac1.png)

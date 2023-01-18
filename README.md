#  Developing a Single Page App with Flask and Vue.js
  The following is a step-by-step walkthrough of how to set up a basic CRUD app with Vue and Flask. We'll start by scaffolding a new Vue application with the Vue CLI and then move on to performing the basic CRUD operations through a back-end RESTful API powered by Python and Flask.

# What are we Building?

1) Our goal is to design a back-end RESTful API, powered by Python and Flask, for a single resource -- books. The API itself should follow RESTful design principles, using the basic HTTP verbs: GET, POST, PUT, and DELETE.

2)We'll also set up a front-end application with Vue that consumes the back-end API:

3) This project is about a Single Page Application, SPAs usually are written using javascript, in this case, 
we used a Javascript Framework called Vue.js, and the frontend depends on a backend written in Python, 
this backend is offering only the basic login features, register, login, and logout. The data is saved into a Microsoft SQL Server database.  

# Objectives

1)Explain what Flask is

2)Explain what Vue is and how it compares to other UI libraries and front-end frameworks like React and Angular

3)Scaffold a Vue project using the Vue CLI

4)Create and render Vue components in the browser

5)Create a Single Page Application (SPA) with Vue components

6)Connect a Vue application to a Flask back-end

7)Develop a RESTful API with Flask

8)Style Vue Components with Bootstrap

9)Use the Vue Router to create routes and render components

# Technologies used 

# 1)Backend 
Python, Flask, SQLAlchemy, virtualenv

# 2)Frontend 
Javascript, Vue.js, Vuetify, Axios

# 3)Database 
 Microsoft SQL Server
 
 This is a Single File component, which is broken up into three different sections:

a) template: for component-specific HTML

b) script: where the component logic is implemented via JavaScript

c) style: for CSS styles

 
 # Main Dependencies
 1)Vue v2.6.11
 
 2)Vue CLI v4.5.11
 
 3)Node v15.7.0
 
 4)npm v7.4.3
 
 5)Flask v1.1.2
  
  6)Python v3.9.1
  
  
 # What is Flask?
   Flask is a simple, yet powerful micro web framework for Python, perfect for building RESTful APIs. Like Sinatra (Ruby) and Express (Node), it's minimal and flexible, so you can start small and build up to a more complex app as needed.

First time with Flask? Check out the following two resources:

 1) Flaskr TDD
 
 2)Developing Web Applications with Python and Flask
 
 # What is Vue?
    Vue is an open-source JavaScript framework used for building user interfaces. It adopted some of the best practices from React and Angular. That said, compared to React and Angular, it's much more approachable, so beginners can get up and running quickly. It's also just as powerful, so it provides all the features you'll need to create modern front-end applications.
 
 
 # Flask Setup
Begin by creating a new project directory:

$ mkdir flask-vue-crud
$ cd flask-vue-crud
Within "flask-vue-crud", create a new directory called "server". Then, create and activate a virtual environment inside the "server" directory:

$ python3.9 -m venv env

$ source env/bin/activate

(env)$

The above commands may differ depending on your environment.

Install Flask along with the Flask-CORS extension:

(env)$ pip install Flask==1.1.2 Flask-Cors==3.0.10

Add an app.py file to the newly created "server" directory:

from flask import Flask, jsonify

from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
    
Why do we need Flask-CORS? In order to make cross-origin requests -- e.g., requests that originate from a different protocol, IP address, domain name, or port -- you need to enable Cross Origin Resource Sharing (CORS). Flask-CORS handles this for us.

It's worth noting that the above setup allows cross-origin requests on all routes, from any domain, protocol, or port. In a production environment, you should only allow cross-origin requests from the domain where the front-end application is hosted. Refer to the Flask-CORS documentation for more info on this.

Run the app:

(env)$ python app.py
To test, point your browser at http://localhost:5000/ping. You should see:

"pong!"
Back in the terminal, press Ctrl+C to kill the server and then navigate back to the project root. With that, let's turn our attention to the front-end and get Vue set up.

# Vue Setup
We'll be using the powerful Vue CLI to generate a customized project boilerplate.

Install it globally:

$ npm install -g @vue/cli@4.5.11

First time with npm? Review the official About npm guide.

Then, within "flask-vue-crud", run the following command to initialize a new Vue project called client:

$ vue create client
This will require you to answer a few questions about the project.

Vue CLI v4.5.11
? Please pick a preset: (Use arrow keys)
❯ Default ([Vue 2] babel, eslint)
  Default (Vue 3 Preview) ([Vue 3] babel, eslint)
  Manually select features
  
Use the down arrow key to highlight "Manually select features", and then press enter. Next, you'll need to select the features you'd like to install. For this tutorial, select "Choose Vue version", "Babel", "Router", and "Linter / Formatter" like so:

Vue CLI v4.5.11
? Please pick a preset: Manually select features
? Check the features needed for your project:
❯◉ Choose Vue version
 ◉ Babel
 ◯ TypeScript
 ◯ Progressive Web App (PWA) Support
 ◉ Router
 ◯ Vuex
 ◯ CSS Pre-processors
 ◉ Linter / Formatter
 ◯ Unit Testing
 ◯ E2E Testing
Press enter.

Select "2.x" for the Vue version. Use the history mode for the router. Select "ESLint + Airbnb config" for the linter and "Lint on save". Finally, select the "In package.json" option so that configuration is placed in the package.json file instead of in separate configuration files.

You should see something similar to:

Vue CLI v4.5.11
? Please pick a preset: Manually select features
? Check the features needed for your project: Choose Vue version, Babel, Router, Linter
? Choose a version of Vue.js that you want to start the project with 2.x
? Use history mode for router? (Requires proper server setup for index fallback in production) Yes
? Pick a linter / formatter config: Airbnb
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, ESLint, etc.? In package.json
? Save this as a preset for future projects? (y/N) No
Press enter again to configure the project structure and install the dependencies.

Take a quick look at the generated project structure. It may seem like a lot, but we'll only be dealing with the files and folders in the "src" folder along with the index.html file found in the "public" folder.

The index.html file is the starting point of our Vue application.


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

$ cd client
$ npm run serve
Navigate to http://localhost:8080 in the browser of your choice. You should see the following:

![jpg](https://user-images.githubusercontent.com/93249038/213129030-c292c63a-4b03-4338-8ceb-5faa6e6c592f.jpg)


# Install the node modules

npm install 

# Install other packages

npm install --save vue-router

npm install bootstrap-vue --save

npm install bootstrap@4.6.0 --save

npm install axios --save

# Run the Frontend

cd frontend

npm run serve
# Run the backend

cd backend( navigating to python files)

conda activate <py38>

python app.py
Check the output in browser

http://localhost:

# Final App

![Screenshot (50)](https://user-images.githubusercontent.com/93249038/213121240-2c32139a-9b45-4f5a-9579-ea13e56cbac1.png)

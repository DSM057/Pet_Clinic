# This is my small pet project 
This site was written with Django framework 

Functional : 

# User Registration:

A new user registration form is implemented, where user name, password and other data are entered.
Upon successful registration, the user's data is stored in the database, which allows to identify and authenticate the user in the future.

# Authentication and Authorisation:

Authentication mechanisms are built in to verify the user details while logging in.
Users can securely log into their account using their credentials, which are verified and matched against records in the database.

# Storing User Information:

Django data models are created to store information about users (including their personal information, accounts, and related content).
Standard Django models such as User are used, as well as custom models such as Client and ClientAnimal to store additional information.

# Manage Appointments and Bookings:

Users can book vet appointments via a form on the website.
Bookings are stored in a database, linked to specific clients and their pets.

# Data Processing and Display:

Implemented functions to extract and display data about users and their records on various pages of the site.
Implemented a mechanism to load additional data via AJAX, allowing the user to retrieve new records without having to reload the page.

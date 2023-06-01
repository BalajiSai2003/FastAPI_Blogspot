# Backend FastAPI_Blogspot app by using FastAPI

#### This API has 3 routes

## 1) Post route

#### This route is responsible for creating a post, deleting a post, updating a post, and searching for a post by ID.

## 2) Users route

#### This route is about creating a user, deleting a user, updating a user, and searching for a user by ID.

## 3) Auth route

#### This route is about the login system.

## Features

* Full **Docker** integration (Docker-based)..
* **Docker Compose** integration and optimization for local development.
* **Secure password** hashing by default.
* **JWT token** authentication.
* **SQLAlchemy** models.

# How to run locally

First, clone this repo by using the following command
````

git clone https://github.com/BalajiSai2003/FastAPI_Blogspot.git

````

Then, navigate to the cloned directory


````

cd FastAPI_Blogspot

````
You need a database in Postgres. Create a database in Postgres, and then create a file named `.env` and write the following configuration in the file


````
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = password_that_you_set
DATABASE_NAME = name_of_database
DATABASE_USERNAME = User_name
SECRET_KEY = 09d25e094faa2556c818166b7a99f6f0f4c3b88e8d3e7
ALGORITHM = HS256

````

Make sure to have Docker installed. Run the following commands



````

docker build -t myimage .

````
````

docker compose up -d

````


Then, you can use the following link to access the API



````

http://127.0.0.1:8000/docs 

````

# how to run locally without Docker
First clone this repo by using following command
````

git clone https://github.com/BalajiSai2003/FastAPI_Blogspot.git

````
then 
````

cd FastAPI_Blogspot

````

Then install fastapp using all flag like 

````

pip install -r requirements.txt

````

Then go this repo folder in your local computer run follwoing command
````

uvicorn main:app --reload

````

Then you can use following link to use the  API

````

http://127.0.0.1:8000/docs 

````

## After run this API you need a database in postgres 
Create a database in postgres then create a file name .env and write the following things in you file 

````
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = password_that_you_set
DATABASE_NAME = name_of_database
DATABASE_USERNAME = User_name
SECRET_KEY = 09d25e094faa2556c818166b7a99f6f0f4c3b88e8d3e7
ALGORITHM = HS256


````
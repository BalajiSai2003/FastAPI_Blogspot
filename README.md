# 
# Backend FastAPI_Blogspot app by using FastAPI

#### This API  has 3 routes

## 1) Post route

#### This route is reponsible for creating post, deleting post, updating post and searching Post by id

## 2) Users route

#### This route is about creating user ,deleting user, updating user and searching user by id

## 3) Auth route

#### This route is about login system

## Features

* Full **Docker** integration (Docker based).
* Docker Swarm Mode deployment.
* **Docker Compose** integration and optimization for local development
* **Secure password** hashing by default.
* **JWT token** authentication.
* **SQLAlchemy** models
# how to run locally
First clone this repo by using following command
````

git clone https://github.com/BalajiSai2003/FastAPI_Blogspot.git

````
then 
````

cd FastAPI_Blogspot

````

Make sure to have docker installed
run the following commands

````

docker build -t myimage .
docker compose up -d

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
DATABASE_PASSWORD = passward_that_you_set
DATABASE_NAME = name_of_database
DATABASE_USERNAME = User_name
SECRET_KEY = 09d25e094faa2556c818166b7a99f6f0f4c3b88e8d3e7 
ALGORITHM = HS256

````

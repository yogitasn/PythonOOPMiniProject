## Table of contents
* [General info](#general-info)
* [Description](#description)
* [Technologies](#technologies)
* [Setup](#setup)
* [Execution](#execution)

## General info
This project is python bank application using OOP mini project.

## Description
Flask-SQLAlchemy is the Flask extension that adds support for SQLAlchemy. Most programming language platforms are object oriented. Data in RDBMS servers on the other hand is stored as tables. Object relation mapping is a technique of mapping object parameters to the underlying RDBMS table structure. An ORM API provides methods to perform CRUD operations without having to write raw SQL statements.


Project is created using Flask-SQLALchemy with MYSQL as Database for storing data. Models are created for Customer, Employees, BankAccount and CreditCard. All the tables are populated using flask-sqlalchemy library functions. User is prompted to enter the Customer ID and option to deposit and withdraw from the Bank Account


## Technologies
Project is created with:
* MySQL Database
* Flask-SQLALchemy
* PyMySQL (Python library connector to communicate with MYSQL )


## Setup
To run this project, install the below libraries

```
$ pip install Flask-SQLAlchemy
$ pip install PyMySQL

```

To update the configuration file 'database.cfg' with your database credentials. Create a database (i.e. create database test) before running the project and pass the value in config file

```
[DATABASE]
DB_USER=
DB_PASSWORD=
DB_PORT=
DATABASE=

```


## Execution

```
python __main__.py

```

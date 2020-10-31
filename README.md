## Table of contents
* [General info](#general-info)
* [Description](#description)
* [Technologies](#technologies)
* [Setup](#setup)
* [Execution](#execution)

## General info
This project is python bank application using OOP mini project.

## Description
Project is created using Flask SQLALchemy with MYSQL as Database for storing data. Models are created for Customer, Employees, BankAccount and CreditCard. All the tables are populated using flask sqlalchemy library functions. User is prompted to enter the Customer ID and option to deposit and withdraw from the Bank Account


## Technologies
Project is created with:
* MySQL Database 
* Flash-SQLALchemy
* PyMySQL (Python library connector to communicate with MYSQL )


## Setup
To run this project, install the below libraries

```
$ pip install Flask-SQLAlchemy
$ pip install PyMySQL

```

To update the configuration file 'database.cfg' with your database credentials.Create a database before running the project and pass the value in config file

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

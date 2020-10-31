from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from BankAccount import BankAccount
import logging
import configparser

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level = logging.INFO)

config = configparser.ConfigParser()
config.read('bankapplication/database.cfg')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:{}/{}'.format(*config['DATABASE'].values())
db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'customer'

    cust_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
   
 
    def __init__(self, cust_id, name,email,phone):
        """ 
        The constructor for Customer class. 
  
        Parameters: 
           name (String): The name of the Customer
           id (int): A unique number to identify the Customer
           email(String): Email id of the Customer
           phone(String): Customer's phone number
        """
        self.cust_id = cust_id
        self.name = name
        self.email = email
        self.phone = phone

    #set the attributes
    def set_name(self, name):
        self.name = name

    def set_id(self, cust_id):
        self.cust_id = cust_id

    def set_department(self, email):
        self.email = email

    def set_title(self, phone):
        self.phone = phone

    #return the attributes
    def get_name(self):
        return self.name

    def get_id(self):
        return self.cust_id

    def get_department(self):
        return self.email

    def get_title(self):
        return self.phone

    def __str__(self):
        return 'Name: ' + self.name + \
               '\nCustomer ID number: ' + self.cust_id + \
               '\nEmail: ' + self.email + \
               '\nPhone: ' + self.phone
    

    def create_customer(self):
        """      
        The function to create a new Customer entry in the database 
    
        Parameters:
               None
       
        Returns:
               None
        """
        db.create_all()
        cust=Customer(self.cust_id,self.name,self.email,self.phone)
        logging.info('New Customer Created Id:{} name:{} email:{} phone:{} '.format(self.cust_id,self.name,self.email,self.phone))
        db.session.add(cust)
        db.session.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
import configparser

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level = logging.INFO)

config = configparser.ConfigParser()
config.read('../database.cfg')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:{}/{}'.format(*config['DATABASE'].values())
db = SQLAlchemy(app)

class Employees(db.Model):
    __tablename__ = 'employees'

    emp_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    department = db.Column(db.String(120))
    title = db.Column(db.String(120)) 
    
    def __init__(self, emp_id,name, department, title):
        """ 
        The constructor for Employee class. 
  
        Parameters: 
           name (String): The name of the Employee
           id (int): A unique number to identify the Employee
           department(String): The department Employee belongs to
           title(String): The title of the Employee
        """
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.title = title

    #set the attributes
    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.emp_id = emp_id

    def set_department(self, department):
        self.department = department

    def set_title(self, title):
        self.title = title

    #return the attributes
    def get_name(self):
        return self.name

    def get_id(self):
        return self.emp_id

    def get_department(self):
        return self.department

    def get_title(self):
        return self.title
    
    def create_employees(self):
        """      
        The function to create a new Employee entry in the database 
       
        Parameters:
               None
       
        Returns:
               None
        """
        
        db.create_all()
        e=Employees(emp_id=self.emp_id,name=self.name,department=self.department,title=self.title)
        logging.info('New Employee Created Id:{} name:{} department:{} title:{} '.format(self.emp_id,self.name,self.department,self.title))
        db.session.add(e)
        db.session.commit()




    
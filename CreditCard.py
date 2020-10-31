from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
import configparser

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level = logging.INFO)

config = configparser.ConfigParser()
config.read('bankapplication/database.cfg')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:{}/{}'.format(*config['DATABASE'].values())
db = SQLAlchemy(app)

class CreditCard(db.Model):
    
    __tablename__ = "creditcard"
    
    title=db.Column(db.String(10),nullable='False')
    first_name=db.Column(db.String(50),nullable='False')
    last_name=db.Column(db.String(50),nullable='False')
    address=db.Column(db.String(100),nullable='False')
    card_number = db.Column(db.Integer,primary_key=True)
    expiration_month = db.Column(db.String(5),nullable='False')
    expiration_year=db.Column(db.Integer,nullable='False')
    security_code = db.Column(db.String(5),nullable='False')
    card_type = db.Column(db.String(20),nullable='False')
    currency_code = db.Column(db.String(10),nullable='False')
    beginning_balance = db.Column(db.Float,nullable='False')
    account_balance = db.Column(db.Float,nullable='False')
    charges = db.Column(db.Float,nullable='False')
    overdraft_fees = db.Column(db.Float,nullable='False')
    payments = db.Column(db.Float,nullable='False')
    ending_balance = db.Column(db.Float,nullable='False')

    def __init__(self,  title = " ", first_name = " ", last_name = " ", address=" ", card_number = 0, exp_month = " ", exp_year = 0, cvv2 = " ", card_type = " ", currency_code = " ", beginning_balance = 0.00, account_balance = 0.00, charges = 0.00, overdraft_fees = 0.00, payments = 0.00, ending_balance = 0.00):
        """ Opens an account. """
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.address=address
        self.card_number = card_number
        self.expiration_month = exp_month
        self.expiration_year = exp_year
        self.security_code = cvv2
        self.card_type = card_type
        self.currency_code = currency_code
        self.beginning_balance = beginning_balance
        self.account_balance = account_balance
        self.charges = charges
        self.overdraft_fees = overdraft_fees
        self.payments = payments
        self.ending_balance = ending_balance
    
    def create_Credit_Account(self):
        """      
        The function to create a new Credit Card entry in the database 
       
        Parameters:
               None
       
        Returns:
               None
        """
        db.create_all()
        credit_card=CreditCard(self.title,self.first_name,self.last_name,self.address,self.card_number,self.expiration_month,self.expiration_year,self.security_code,self.card_type,self.currency_code,self.beginning_balance,self.account_balance,self.charges,self.overdraft_fees,self.payments,self.ending_balance)
        logging.info('New Credit Card Account created : Card Number {}'.format(self.card_number))
        db.session.add(credit_card)
        db.session.commit()

    def create_beginning_balance(self, card_number,amount):
        """      
        The function to establish a begining balance for a credit card
       
        Parameters: 
                card_number (int): Credit card number of the Customer
                amount(int): The amount to create the begining balance
       
        Returns:
               None
        """

        creditCard = CreditCard.query.filter_by(card_number=self.card_number).first()
        creditCard.beginning_balance+=amount
        db.session.commit()
        creditCard.account_balance+=amount
        db.session.commit()
        creditCard.ending_balance+=amount
        db.session.commit()
    
        self.ending_balance += amount
        db.session.commit()

    def create_charges(self, card_number,amount):
    
        """      
        The function to Reduces the amount from the account balance. Each charge resulting in an over draft negative account balance
        Also deducts a fee of 25 dollars from the account balance.
       
        Parameters: 
                card_number (int): Credit card number of the Customer
                amount(int): The amount to create the begining balance
       
        Returns:
               None
        """
        creditCard = CreditCard.query.filter_by(card_number=self.card_number).first()

        creditCard.account_balance -= amount
        creditCard.ending_balance -= amount
        db.session.commit()

        if creditCard.account_balance < 0:
            creditCard.account_balance -= 25
            creditCard.ending_balance -= 25
            creditCard.overdraft_fees += 25
        db.session.commit()

    def create_payments(self, card_number,amount):
        """      
        The function to Deposits the amount into the account balance.
       
        Parameters: 
                card_number (int): Credit card number of the Customer
                amount(int): The amount to create the begining balance
       
        Returns:
               None
        """
        
        creditCard = CreditCard.query.filter_by(card_number=self.card_number).first()

        creditCard.account_balance += amount
        creditCard.ending_balance += amount
        creditCard.payments += amount
        db.session.commit()
               
    def display_beginning_balance(self):
        """ Returns the beginning balance. """
        print ("Beginning Balance: %s" % str(self.beginning_balance))

    def display_charges(self):
        """ Returns total charges. """
        print ("- Charges:         %s" % str(self.charges))
         
    def display_fees(self):
        """Returns the total fees."""
        print ("- Overdraft Fees:   %s" % str(self.overdraft_fees))

    def display_payments(self):
        """ Returns total payments. """
        print ("+ Payments:        %s" % str(self.payments))
    
    def display_account_balance(self):
        """ Returns the account balance. """
        print ("Account Balance:    %s" % str(self.account_balance))

    def display_ending_balance(self):
        """ Returns the ending balance. """
        print ("Ending Balance:    %s" % str(self.ending_balance))

    def __str__(self):
        s = "Account:                  %s\n" % (self.account)
        s += "Beginning Balance: %s\n" % (self.beginning_balance)
        s += "- Charges:               %s\n" % (self.charges)
        s += "- Overdraft Fees:     %s\n" % (self.overdraft_fees)
        s += "+ Payments:            %s\n" % (self.payments)
        s += "Ending Balance:       %s\n" % (self.ending_balance)
        return s
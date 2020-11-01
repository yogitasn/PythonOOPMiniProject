from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
import configparser

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level = logging.INFO)

config = configparser.ConfigParser()
config.read('../bankapplication/database.cfg')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:{}/{}'.format(*config['DATABASE'].values())
db = SQLAlchemy(app)

class BankAccount(db.Model):

    __tablename__ = "bankaccount"

    bank_acc_no = db.Column(db.Integer, primary_key=True)
    cust_id = db.Column(db.Integer, primary_key=True)
    actnType= db.Column(db.String(50),nullable='False') 
    money= db.Column(db.Float,nullable='False') 
    penalty_amount = 5




    def __init__(self,bank_acc_no=0,cust_id=0,actnType=" ",initial_balance=0.00):
            """ 
            The constructor for BankAccount class. 
    
            Parameters: 
            bank_acc_no (Integer): The Account number of the Customer
            cust_id (Integer): Customer Id of the Customer
            actnType (AccountType): Account Type of the Bank Account of the Customer
            balance(float): Balance amount in the Account of the Customer
            """
            self.bank_acc_no=bank_acc_no
            self.cust_id=cust_id
            self.actnType= actnType
            self.money = initial_balance
            self.penalty = 0
            
    

    def getAccountNo(self):

       return self.bank_acc_no

    def getAcccountHolderId(self):

       return self.cust_id

    def getAccountType(self):

       return self.actnType

    def getBalance(self):

       return self.money
    def deposit(self,cust_id,amount):
        """      
        The function to deposit a amount to a Bank Account.
       
        Parameters:
               amount (Integer): The amount to be deposited
       
        Returns:
               Balance: The new balance amount
        """
        
        bankAcc = BankAccount.query.filter_by(cust_id=self.cust_id).first()
        logging.info('Previous Balance is : {} '.format(bankAcc.money))
        bankAcc.money=bankAcc.money+amount
        db.session.commit()
        logging.info('New Balance is : {} '.format(bankAcc.money))


    def withdraw(self,cust_id,amount):
        """      
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
     
       
        Parameters:
               amount (Integer): The amount to be withdrawn
       
        Returns:
               Balance: The new balance amount
        """
    
        bankAcc = BankAccount.query.filter_by(cust_id=cust_id).first()
        logging.info('Previous Balance is : {} '.format(bankAcc.money))
     
        if bankAcc.money - amount < 0:
            logging.warn('The account balance is less than zero')
            bankAcc.money -= (amount + BankAccount.penalty_amount)
            bankAcc.money += BankAccount.penalty_amount

        else:
            bankAcc.money -= amount
        logging.info('New Balance is : {} '.format(bankAcc.money))
     
        db.session.commit()
        

    def create_Bank_Account(self):
        """      
        The function to create a new Bank Account entry in the database 
       
        Parameters:
               None
       
        Returns:
               None
        """
        db.create_all()
        bank_account=BankAccount(self.bank_acc_no,self.cust_id,self.actnType,self.money)
        db.session.add(bank_account)
        logging.info('New Bank Account Created Id:{} Customer ID:{} Account Type:{} money:{} '.format(self.bank_acc_no,self.cust_id,self.actnType,self.money)) 
        db.session.commit()

    def drop_Bank_Account(self):
       """      
        The function to drop Bank Account table  
       
        Parameters:
               None
       
        Returns:
               None
        """
       db.drop_all()
       logging.info('Bank Account Table dropped')
        

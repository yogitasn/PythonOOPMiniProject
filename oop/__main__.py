from flask import current_app as app
from Employees import db, Employees
from Customer import Customer
from BankAccount import BankAccount
from CreditCard import CreditCard

def populate_database():
    """Populate the database."""
    emp=Employees(123456,'Sammy','Retail Applications','IT Analyst')
    emp1=Employees(5678,'Nancy','Capital Market','Teller')
    emp.create_employees()
    emp1.create_employees()

    cust=Customer(123,'John','john.s@gmail.com','1-233-2234')
    cust1=Customer(5678,'Katherine','katherine.k@yahoo.com','1-456-4578')
    cust2=Customer(6788,'Vijay','vijay.raj@gmail.com','1-678-5555')
    cust.create_customer()
    cust1.create_customer()
    cust2.create_customer()

    bank_Acc=BankAccount(1234444,123,'Chequing',100)
    bank_Acc.create_Bank_Account()
    
    bank_Acc1=BankAccount(567888,5678,'Saving',200)
    bank_Acc1.create_Bank_Account()

    bank_Acc2=BankAccount(1677777,6788,'Chequing',400)
    bank_Acc2.create_Bank_Account()


    creditCard=CreditCard('Ms','Nancy','Smith','15 Bloor St, Toronto',14566666,'May',2023,'677','Visa','CAD')
    creditCard.create_Credit_Account()
    creditCard1=CreditCard('Mr','Sam','Rogers','15 Upland St, Toronto',8999666,'Aug',2021,'127','Visa','CAD')
    creditCard1.create_Credit_Account()


def main():
    populate_database()
    while True:
         try:
            # To Test please use 123,5678 or 6788
            
            customer_id=input("Please enter customer ID: ")
            if not customer_id:
                break
            choice=int(input("Please enter 1-Deposit or 2-Withdraw: "))
            if choice==1:
                b=BankAccount(cust_id=customer_id)
                amt=int(input("Please enter the amount to deposit: "))
                b.deposit(cust_id=customer_id,amount=amt)
        
            elif choice==2:
                b=BankAccount(cust_id=customer_id)
                amt=int(input("Please enter the amount to withdraw: "))
                b.withdraw(cust_id=customer_id,amount=amt)
         except ValueError:
                print("Oops!  Invalid values  Try again...")


    
if __name__ == "__main__":
    main()
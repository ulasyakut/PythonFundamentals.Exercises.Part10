class Person():
    def __init__(self,id,first_name,last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account():
    def __init__(self,number,type,owner,balance=0):
        self.number = number
        self.type =type
        self.owner = owner
        self.balance = balance

class Bank():
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self,id,first_name,last_name):
        if id in self.customers:
            print('customer already exist')
        else:
            new_customer = Person(id,first_name,last_name)
            self.customers[id] = new_customer
            print('Customer added')


    def add_account(self,type,id):
        if id not in self.customers: 
            print('customer is not registered')
        else:
            self.accounts[id] = type

    def remove_account(self,id):
        if id not in self.accounts:
            print('account doesnt exist')
        else:
            del self.accounts[id]

    def deposit_money(self,balance):

        add = input('amount: ')
        balance +=add

    def withdraw_money(self,balance):
        subtract = input('amount: ')
        balance -=subtract

    def balance_inquiry():
        pass


        

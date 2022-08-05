class Account:
    
    def __init__(self,owner,balance=0):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"Account {self.owner}: Balance: {self.balance}."
    
    def deposit(self,val):
        self.balance += val
        #print(f"Deposit Accepted! {val} add to account!")
        
    def withdraw(self,val):
        if self.balance >= val : 
            self.balance -= val
            #print("Withdraw processed!")
        else:
            print("Insufficient funds!")
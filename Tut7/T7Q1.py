class BankAccount:
    count=0
    def __init__(self,a,b):
        self.name=a
        self.bal=b
        BankAccount.count += 1
    def __str__(self):
        return '%s has %i in the account' %(self.name,self.bal)
    @staticmethod
    def displayTotalAccount():
        print('Total number of account created is %i' %(BankAccount.count))
    def setBalance(self,i):
        self.bal=i
    def getBalance(self):
        return self.bal
    def withdraw(self,i):
        if (i>self.bal):
            print('Balance is insufficient')
        else:
            self.bal-=i
            print('Balance is sufficient')
    def deposit(self,i):
        self.bal+=i
    

a1 = BankAccount("Abu", 100)
b1 = BankAccount("Ali", 200)
BankAccount.displayTotalAccount() 
print(a1)
a1.withdraw(200) 
a1.withdraw(50)
print(a1.getBalance())
a1.deposit(100)
print(a1.getBalance()) 
a1.setBalance(50)
print(a1.getBalance()) 
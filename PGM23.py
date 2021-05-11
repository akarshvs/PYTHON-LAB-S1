"""
3. Create a Bank account with members account number, name, type of account and balance. Write methods to deposit at the bank and withdraw an amount from the bank.
"""
class Account:
    def __init__(self, acnum):
        print(f'\n---APPLICATION FORM---\nA/C No: {acnum}')
        self.acnum = acnum
        self.name = input('NAME: ')
        self.actype = input('ACCOUNT TYPE: ')
        self.balance = float(input('INITIAL DEPOSIT: '))
    def vbalance(self):
        print(f'CURRENT BALANCE: {self.balance:.2f}')
    def deposit(self):
        self.balance += float(input('AMOUNT(DEPOSIT): '))
        self.vbalance()  
    def withdraw(self):
        amount =  float(input('AMOUNT(WITHDRAW): '))
        if self.balance >= amount:
            self.balance -= amount
            self.vbalance()  
        else:
             print('--NOT ENOUGH BALANCE!--')
    def greet(self):
        print(f'\nHello {self.name}!\nA/C No: {self.acnum}\nA/C Type: {self.actype}')

mbr1 = Account(1001)
mbr1.greet()
mbr1.deposit()
mbr1.withdraw()

#BANK EMULATION
"""
# OPERATIONS
def atm(acnum):
    while True:
        choice = int(input('\n1.VIEW BALANCE\n2.DEPOSIT\n3.WITHDRAW\n4.EXIT\nCHOICE: '))
        if choice == 1:
            bank[acnum].vbalance()
        elif choice == 2:
            bank[acnum].deposit()
        elif choice == 3:
            bank[acnum].withdraw()
        elif choice == 4:
            break
        else:
            print('INVALID CHOICE!')

#CREATE ACCOUNT = 3
bank = {}
for acnum in range(1001,1004):
    bank[acnum] = Account(acnum)

#LOGIN USING AC NO
while True:
    try:
        choice = int(input('\n--PRESS 1 TO LOGIN--\n--PRESS ANY OTHER KEY TO EXIT--\nCHOICE: '))
        if choice == 1:
            try:
                acnum = int(input('ENTER A/C No(LOGIN): '))
                bank[acnum].greet()
                atm(acnum)
            except KeyError:
                print('INVALID LOGIN!')
        else:
            print('THANK YOU!')
            break
    except ValueError:
        print('THANK YOU!')
        break

"""

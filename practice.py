class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        print('executed')
        self.menu()


    def menu(self):

        user_input=input(
            'Welcome to ATM system\n' 
        'Hi how can i help you\n' \
        '1-Press 1 to create Pin\n' \
        '2-Press 2 to change pin\n' \
        '3-Press 3 to check balance\n' \
        '4-Press 4 to add money\n' \
        '5-Press 5 to withdraw money\n'
        '6-Anything else to exit'
        ''
        "Enter your choice:")

        if user_input=="1":
            self.createpin()
        elif user_input=="2":
            self.changepin()

        elif user_input=="3":
            self.checkbp()

        elif user_input=="4":
            self.deposit()
        elif user_input=="5":
            self.withdraw()
        else:
            exit()

        
    def createpin(self):
        pin=input("Enter your pin:")
        self.pin=pin
        balance=int(input("Enter Balance:"))
        self.balance=balance
        print("Pin created successfully")

        self.menu()

    def changepin(self):
        old=input("enter old pin:")
        if old==self.pin:
            new=input("enter new pin:")
            self.pin=new
            print("pin changed successfully")
    
        else:
            print("incorrect pin")
        self.menu()


    def checkbp(self):
        print(f"Your current pin is {self.pin}")
        print(f"your cuurent balance is {self.balance}")

        self.menu()

    def deposit(self):
        bal=int(input("enter balance u want to deposit:"))
        self.balance=self.balance+bal
        print(f"Now your balance is {self.balance}")

        self.menu()


    def withdraw(self):
        mon=int(input("enter money u want to withdraw:"))
        self.balance=self.balance-mon
        print(f"Your current balance is now {self.balance}")

        self.menu()

a=Atm()
class AtmMachine:
    # Constructor ( special function) -> superpowers
    # self means it's a function of AtmMachine
    def __init__(self):
        # data property
        print(id(self))
        self.pin = ""
        self.balance = 0
      #  self.menu()

    def menu(self):
        user_input = input(
        """
        Hi how can i help you ?

        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything to exit
        """
        )

        if user_input == "1":
            #create a pin
            self.create_pin()
        elif user_input == "2":
            #change pin
            self.change_pin()
        elif user_input == "3":
            #check balance 
            self.check_balance()
        elif user_input == "4":
            #change withdraw
           # pass
           self.withdraw_balance()

        else:
            exit()
    def create_pin(self):   # putting argument as a self in the function that means it's a function of the class
        user_pin = input("Enter your pain: ")
        self.pin = user_pin

        user_balance = int(input("Enter Balance: "))
        self.balance = user_balance

        print("Pin Created Successfully!")
        self.menu()  # it's a converstion between two methods

    
    def change_pin(self):
        old_pin = input("Enter your old pin: ")

        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Pin changed successfully!")
            self.menu()
        else:
            print("Invalid pin!")
            self.menu()
            
    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Your pin is incorrect, please try again")
        self.menu()

    def withdraw_balance(self):
        user_pin = input("Enter the pin: ")
        if user_pin == self.pin:
            # allow to withdraw
            amount = int(input("Enter the amount : "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"You have withdraw {amount}. your new balance is {self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Your pin is incorrect, please try again")
        self.menu()





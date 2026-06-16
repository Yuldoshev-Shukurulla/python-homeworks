# # ## Model a Farm

# # In this assignment, you’ll create a simplified model of a farm. As you work through this assignment, keep in mind that there are a number of correct answers.

# # The focus of this assignment is less about the Python class syntax and more about software design in general, which is highly subjective. This assignment is intentionally left open-ended to encourage you to think about how you would organize your code into classes.

# # Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes, attributes, and methods. Think about inheritance. How can you prevent code duplication? Take the time to work through as many iterations as you feel are
# # necessary.

# # The actual requirements are open to interpretation, but try to adhere to these guidelines:

# # 1. You should have at least four classes: the parent `Animal` class, and then at least three child animal classes that inherit from Animal.
# # 2. Each class should have a few attributes and at least one method that models some behavior appropriate for a specific animal or all animals—such as walking, running, eating, sleeping, and so on.
# # 3. Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviors.

# # ---

class Animal:

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
class Cow(Animal):
    
    def __init__(self, name, age, species, milk_production):
        self.milk = milk_production
        super().__init__(name, age, species)

    def sound(self):
        print("Moox!")
    
    def produce_milk(self):
        print(f"{self.name} produces {self.milk} liter of milk every day.")
    
class Dog(Animal):

    def __init__(self, name, age, species,breed):
        self.breed = breed
        super().__init__(name, age, species)
    
    def bark(self):
        print(f'{self.name} is barking: Vov-vov!')
    
    def guard_farm(self):
        print(f"{self.name}(Breed: {self.breed}) is guarding a farm.")
    
class Chicken(Animal):
    def __init__(self, name, age, species, egg_count):
        self.egg_count = egg_count
        super().__init__(name, age, species)
        
    def lay_egg(self):
        print(f"{self.name} laid {self.egg_count} eggs today!")

if __name__ == "__main__":
    print("--- Creating Farm Animals ---")
    
    cow1 = Cow("Oqtosh", 4, "Mammal", 15)
    dog1 = Dog("Simba", 2, "Mammal", "German Shepherd")
    chicken1 = Chicken("Pishka", 1, "Bird", 2)
    
    print("\n[Cow Section]")
    cow1.eat()           
    cow1.sound()         
    cow1.produce_milk()  
    
    print("\n[Dog Section]")
    dog1.sleep()     
    dog1.bark()         
    dog1.guard_farm()  
    
    print("\n[Chicken Section]")
    chicken1.eat()       
    chicken1.lay_egg()   

# # ## Build a Bank Application

# # #### **Objective:**
# # Develop a command-line banking application that allows users to perform basic banking operations like creating an account, depositing money, and withdrawing money. This will help you practice using object-oriented programming (OOP), file handling, and error handling in Python.


# # ### **Tasks:**

# # #### **Step 1: Define the Classes**
# # 1. Create a class `Account` with attributes:
# #    - `account_number`
# #    - `name`
# #    - `balance`

# # 2. Create a class `Bank` to manage all accounts. It should have:
# #    - A dictionary to store accounts (`accounts`).
# #    - Methods for each operation:
# #      - `create_account(name, initial_deposit)`
# #      - `view_account(account_number)`
# #      - `deposit(account_number, amount)`
# #      - `withdraw(account_number, amount)`
# #      - `save_to_file()` and `load_from_file()` (for file handling).


# # #### **Step 2: Implement the Methods**
# # 1. **Account Creation**
# #    - Generate a unique `account_number`.
# #    - Create an `Account` object and store it in the dictionary.
# #    - Save account details to a file.

# # 2. **View Account Details**
# #    - Prompt the user to input their account number.
# #    - Retrieve and display the account details if found; otherwise, show an error.

# # 3. **Deposit Money**
# #    - Prompt the user for their account number and deposit amount.
# #    - Validate the amount and update the account balance.

# # 4. **Withdraw Money**
# #    - Prompt the user for their account number and withdrawal amount.
# #    - Validate that the amount is less than or equal to the balance and update the account balance.

# # 5. **File Handling**
# #    - Use `save_to_file` to write account details to `accounts.txt`.
# #    - Use `load_from_file` to load account details when the program starts.

# # ---

import random
import json
import os

filename = 'accounts.txt'
os.chdir('C:\\a62ab832e6d116c5594b4b3659421f\sh\python-homeworks\lesson-8')
class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def to_dict(self):
        return {
            "account_number" : self.account_number,
            "name" : self.name,
            "balance" : self.balance
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            account_number = data['account_number'],
            name = data['name'],
            balance = data['balance']
        )
    
class Bank:
    def __init__(self):
        self.accounts = {} 

    def create_account(self, name, initial_deposit):
        account_number = str(random.randint(100000, 999999))
        if initial_deposit >= 0:
            new_account = Account(account_number, name, initial_deposit)
            self.accounts[account_number] = new_account
            print(f"Account created successfully! Number: {account_number}")
            self.save_to_file()
            return account_number
        else:
            print("Initial deposit cannot be negative!")
            return None

    def view_account(self, account_number):
        if account_number in self.accounts:
            account =self.accounts[account_number]
            print(f"\n--- Account Details ---")
            print(f"Account Number: {account.account_number}")
            print(f"Account Holder: {account.name}")
            print(f"Current Balance: {account.balance} UZS")
        else:
            print(f"Error: Account number {account_number} not found!")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if amount > 0:
                account.balance += amount
                print(f"Successfully deposited {amount} UZS. New balance: {account.balance} UZS")
                self.save_to_file()
            else:
                print('Amount should bu positive.')
        else:
            print(f"Error: Account number {account_number} not found!")
        
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if 0 < amount <= account.balance:
                account.balance -= amount
                print(f"Successfully withdrew {amount} UZS. Remaining balance: {account.balance} UZS")
                self.save_to_file()
            elif amount > account.balance:
                print("Error: Not enough money on balance.")
            else:
                print("Error: Amount should be positive.")
        else:
            print(f"Error: Account number {account_number} not found!")
        
    def save_to_file(self):
        data_to_save = {acc_num: acc_obj.to_dict() for acc_num, acc_obj in self.accounts.items()}
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, indent=4)
        print(f'Data saved succesfullyto {filename}')
    
    def load_from_file(self):
        if not os.path.exists(filename):
            return
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
                self.accounts = {acc_num: Account.from_dict(acc_data) for acc_num, acc_data in raw_data.items()}
        except (json.JSONDecodeError, KeyError):
            print("Error loading file or file is corrupted. Starting with empty bank.")
    
def main():
    bank = Bank()
    bank.load_from_file()   
    print('Welcome to the Bank Application!')
    while True:
        print('''Choose your choice:
                1. Add a new account
                2. View account details
                3. Deposit money
                4. Withdraw money
                5. Exit''')
        
        choice = input('Enter your choice: ').strip()
        if choice == '1':
            username = input('Enter your name: ').strip()
            try:
                amount1 = int(input('Enter initial amount: ').strip())
                bank.create_account(username, amount1)
            except ValueError:
                print('Enter valid initial amount.')
        elif choice == '2':
            username = input('Enter account number: ').strip()
            bank.view_account(username)
        elif choice == '3':
            username = input('Enter account number: ').strip()
            try:
                amount1 = int(input('Enter deposit amount: ').strip())
                bank.deposit(username, amount1)
            except ValueError:
                print('Enter valid deposit amount.')
        elif choice == '4':
            username = input('Enter account number: ').strip()
            try:
                amount1 = int(input('Enter withdrawal amount: ').strip())
                bank.withdraw(username, amount1)
            except ValueError:
                print('Enter valid withdrawal amount.')
        elif choice == '5':
            bank.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid alternative selection. Try again.")

if __name__ == "__main__":
    main()
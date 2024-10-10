import random

class Account:

    def __init__(self):
        self.HolderName = None
        self.AccNumber = None
        self.Password = None
        self.dob = None
        self.Phone = None
        self.Address = None
        self.balance = None
        self.details = {
            "HolderName": None,
            "AccNumber": None,
            "Password": None,
            "dob": None,
            "Phone": None,
            "Address": None,
            "Balance": 0
        }
        self.database = {}

    def main_menu(self):
        while True:
            print("TechMahindra Bank Ltd.")
            print("\n1. Create Account\n2. View Account Details\n3. Withdraw\n4. Deposit\n5. Fund Transfer\n6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.CreateAccount()
            elif choice == '2':
                self.Account_info()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.deposit()
            elif choice == '5':
                self.fund_transfer()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please try again.")

    def CreateAccount(self):
        print("Welcome To TechMahindra Bank Ltd.")
        self.details["HolderName"] = input("Enter your name as per Aadhar card: ")
        self.details["dob"] = input("Enter your DOB as per Aadhar card: ")
        self.details["Phone"] = input("Enter your Phone Number: ")
        self.details["Address"] = input("Enter your House Address: ")
        self.details["AccNumber"] = random.randint(1000000, 10999999)
        self.details["Balance"] = 0

        print("Account Created successfully")
        print("Your Account Number is:", self.details["AccNumber"])

        if self.details["AccNumber"] not in self.database:
            self.database[self.details["AccNumber"]] = self.details.copy()

    def withdraw(self):
        Acc = int(input("Enter Account Number:"))
        if Acc not in self.database:
            print("Account not found!")
            return

        money = int(input("Enter amount to withdraw:"))

        if self.database[Acc]["Balance"] >= money:
            self.database[Acc]["Balance"] -= money
            print("Withdrawal successful! Current Balance:", self.database[Acc]["Balance"])
        else:
            print("Insufficient Balance")

    def deposit(self):
        Acc = int(input("Enter Account Number:"))
        if Acc not in self.database:
            print("Account not found!")
            return

        money = int(input("Enter amount to deposit:"))
        self.database[Acc]["Balance"] += money
        print("Deposit successful! Current Balance:", self.database[Acc]["Balance"])

    def fund_transfer(self):
        sender = int(input("Enter your account number:"))
        receiver = int(input("Enter payee account number:"))

        if sender not in self.database or receiver not in self.database:
            print("One or both account numbers not found!")
            return

        money = int(input("Enter Amount to transfer:"))

        if self.database[sender]["Balance"] >= money:
            self.database[sender]["Balance"] -= money
            self.database[receiver]["Balance"] += money
            print("Transaction Successful!!")
        else:
            print("Insufficient Balance in sender's account")

    def Account_info(self):
        acc = int(input("Enter Account Number:"))
        if acc in self.database:
            print(self.database[acc])
        else:
            print("Account not found!")

if __name__ == "__main__":
    account = Account()
    account.main_menu()
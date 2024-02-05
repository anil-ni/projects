
import getpass
import os
import time


def clear(): return os.system('cls')


clear()


def atm_system():
    print('''
             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
             !!!                              !!!
             !!! Welcome to Hamro ATM Service !!!
             !!!                              !!!
             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
             '''.center(150))


account_balance = 50000

time.sleep(2)
pin_code = 2345
atm_system()


atm_pin = int(input("Enter your PIN:\n".center(100)))
time.sleep(2)
clear()
if pin_code == atm_pin:
    while True:
        clear()
        atm_system()
        print('''
            
            1: Check Balance
            2: Deposit Balance
            3: Withdraw Balance
            4: Exit
            '''.center(100))

        option = int(input("Enter the option:\n".center(100)))
        if option == 1:
            print(f"Your Current Balance is,   {account_balance}  ")
            time.sleep(2)

        elif option == 2:
            amount_deposit = int(
                input("Enter the amount you want to deposit:\n"))
            print(f" Your balance is  {amount_deposit+account_balance} ")
            time.sleep(2)

        elif option == 3:
            withdraw = int(input("Enter the amount you want to withdraw:\n"))
            if withdraw > account_balance:
                print("Insufficient Balance!!!")
                time.sleep(2)

            elif withdraw < 1000:
                print("Enter Balance More than 1000")
                time.sleep(2)

            else:
                print(
                    f"The remaining balance is   {account_balance-withdraw  }")
                time.sleep(2)

        elif option == 4:
            print('''
                  Thank You !!!
                  Please Visit Again.
                  ''')
            time.sleep(2)
            exit()

        else:
            print("Please enter valid number!!!")
            time.sleep(1)

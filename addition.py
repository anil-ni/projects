import os
import time


def clear(): return os.system('cls')


def Add_numbers(num1, num2):
    sum = num1 + num2
    return sum


def Sub_numbers(num1, num2):
    substract = num1 - num2
    return substract


def Multi_ply(num1, num2):
    multiply = num1 * num2
    return multiply


def total_result():
    first = float(input("Enter number first: "))
    second = float(input("Enter number second: "))

    return first, second


while True:
    print('''
          Enter the choice:
          1: Add
          2:Substract
          3: Multiply
          4: Exit
          ''')

    option = int(input("Enter the option: "))

    if option == 1:
        add_result = total_result()
        print("Total is: ", Add_numbers(*add_result))
        time.sleep(1)
        clear()
    elif option == 2:
        sub_result = total_result()
        print("Total is: ", Sub_numbers(*sub_result))
    elif option == 3:
        multiply_result = total_result()
        print("Total is: ", Multi_ply(*multiply_result))
    elif option == 4:
        exit()
    else:
        print("Please enter the valid number!!")
        clear()
        break

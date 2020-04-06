#!/usr/bin/env python3
import math 

def calculate():
    global operation
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for square root
sin for trigonometric ratios of sine
cos for trigonometric ratios of cosine
exp for to get exponencial
After select your operation press Enter
''')
    
    if operation == '**':
        onevalue()
        sqr = val ** (1/2)
        print(sqr)
    
    if operation == 'sin':
        onevalue()
        print(math.sin(val))
    
    if operation == 'cos':
        onevalue()
        print(math.cos(val))
    
    if operation == 'exp':
        onevalue()
        print(math.exp(val))
    
    #Addition
    if operation == '+':
        twovalue()
        print('{} + {}  = '.format(number_1, number_2))
        print(number_1 + number_2)
        
    # Subtraction
    elif operation =='-':
        twovalue()
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        
    # Multiplication
    elif operation =='*':
        twovalue()
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        
    # Division
    elif operation =='/':
        twovalue()
        try:
            result = number_1 / number_2
        except ZeroDivisionError:
            print("Zero Division!")
            return again()
        print('{} / {} = '.format(number_1, number_2))
        print(result)
        
    again()

 

# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()

def welcome():
    print('''
Welcome to Calculator write in Python
''')

def onevalue():
    global val
    val_1 = input('Enter Value: ')
    try:
        val = int(val_1)
        #val > 0 
    except ValueError:
        print("You must enter an integer value.")
        return again()

def twovalue():
    global number_1
    global number_2
    val_1 = input('Enter Your first Number: ')
    val_2 = input('Enter Your second Number: ')
    
    try:
        val = int(val_1) and int(val_2)
    except ValueError:
        print("You must enter an integer value.")
        return again()
    
    number_1 = int(val_1)
    number_2 = int(val_2)
    

# Call calculate() outside of the function
welcome()
calculate()




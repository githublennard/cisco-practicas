import math 

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for square root
sin for trigonometric ratios of sine
cos for trigonometric ratios of cosine
After select your operation press Enter
''')
    #number_1 = int(input('Enter Your first Number: '))
    #assert number_1 >=0.0
    val_1 = input('Enter Your first Number: ')
    #number_2 = int(input('Enter Your second Number: '))
    val_2 = input('Enter Your second Number: ')
    
    try:
        #print(number_1)
        val = int(val_1) and int(val_2)
        #val > 0 
    except ValueError:
        print("You must enter an integer value.")
        return again()
    
    number_1 = int(val_1)
    number_2 = int(val_2)
    
    #Addition
    if operation == '+':
        print('{} + {}  = '.format(number_1, number_2))
        print(number_1 + number_2)
        
    # Subtraction
    elif operation =='-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        
    # Multiplication
    elif operation =='*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        
    # Division
    elif operation =='/':
        try:
            result = number_1 / number_2
        except ZeroDivisionError:
            print("Zero Division!")
            return again()
        print('{} / {} = '.format(number_1, number_2))
        print(result)
        #return result
        #print('{} / {} = '.format(number_1, number_2))
        #print(number_1 / number_2)
                
    else:
        print('You have not typed a valid operator, please run the program again.')

 # Add again() function to calculate() function
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

# Call calculate() outside of the function
welcome()
calculate()


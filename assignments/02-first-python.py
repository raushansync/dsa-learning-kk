"""
## Write Java programs for the following:

1. Write a program to print whether a number is even or odd, also take
input from the user.
2. Take name as input and print a greeting message for that particular name.
3. Write a program to input principal, time, and rate (P, T, R) from the user and
find Simple Interest.
4. Take in two numbers and an operator (+, -, *, /) and calculate the value.
(Use if conditions)
5. Take 2 numbers as input and print the largest number.
6. Input currency in rupees and output in USD.
7. To calculate Fibonacci Series up to n numbers.
8. To find out whether the given String is Palindrome or not.
9. To find Armstrong Number between two given number.

"""

# 1. Write a program to print whether a number is even or odd, also take input from the user.

def OddOrEven():
    '''a program to print whether a number is even or odd'''
    user_input = input("Enter a number to check wether it is odd or even: ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Enter a valid number to check.")
        return OddOrEven()
    if user_input % 2 == 0:
        print("Even")
        return
    else:
        print("Odd")
    
OddOrEven()
    
# 2. Take name as input and print a greeting message for that particular name.

def greet():
    '''A program which takes name as input and print a greeting message for that particular name.'''
    user_name = input("Enter Your Name: ")
    user_name = str(user_name)
    print(f"Good Morning! {user_name}")

greet()

# 3. Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest. 

def simpleInterest():
    '''A program to input principal, time, and rate from the user and find Simple Interest.'''
    principal = input("Enter P: ")
    time = input("Enter T (In Years): ")
    rate = input("Enter R: ")
    try:
        principal, time, rate = float(principal), float(time), float(rate)
    except ValueError:
         print("Enter Integer or Decimal Value.")
         simpleInterest()

    print((principal * time * rate) / 100)

simpleInterest()

# 4. Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if condition.)

def calculate():
    '''Taking in two numbers and an operator and calculating the value.'''
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    try:
        first_num, second_num = float(first_num), float(second_num)
    except ValueError:
        print("First Number and Second Number Should be Integer or Decimal.")
        return calculate()
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator == "+":
            print(f"Sum of first number and second number is {first_num + second_num}")
            break
        elif operator == "-":
            print(f"Difference of first number and second number is {first_num - second_num}")
            break
        elif operator == "*":
            print(f"Product of first number and second number is {first_num * second_num}")
            break
        elif operator == "/":
            print(f"Division of first number with second number is {first_num / second_num}")
            break
        else:
            print("Enter a valid operator.")

calculate()

# 5 Take 2 numbers as input and print the largest number.

def largerNumber():
    '''Taking 2 numbers as input and printing the larger number.'''
    first_number = input("Enter first number: ")
    second_number = input("Enter second number: ")
    try:
        first_number, second_number = float(first_number), float(second_number)
    except ValueError:
        print("First number and Second number should be integer or decimal.")
        largerNumber()
    print(f"Larger number is {max(first_number, second_number)}")

largerNumber()# this is the thing we need to improve in this sequence and the way they are doing this is crazy 

# 6. Input currency in rupees and output in USD.

def rupeeToUSD():
    '''Taking input currency in rupees and providing output in USD'''
    rupee = input("Enter rupee: ")
    try:
        rupee = float(rupee)
    except ValueError:
        print("Enter Rupee in Integer or Decimal.")
        return rupeeToUSD()
    print(f"{rupee} Rupee in USD equals {rupee/94}")

rupeeToUSD()


# 7. To calculate Fibonacci Series up to n numbers.

def nFibonacci():
    '''Calculating Fibonacci Series up to n numbers.'''
    n = input("Enter an integer here to get that number of fibonacci numbers: ")
    try:
        n = int(n)
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Enter an Positive Integer to get that many numbers in Fibonacci Series.")
        nFibonacci()

    lis = [0,1]
    if n == 1:
        print(0)
    elif n == 2:
        print(0, 1)
    else:
        print(lis[0])
        print(lis[1])
        for i in range(n-2):
            result = lis[-1] + lis[-2]
            print(result)
            lis.append(result)

nFibonacci()

# 8 To find out whether the given String is Palindrome or not.

def palindromeOrNot():
    tocheck = input("Enter a string to check wether it is a palindrome or not: ")
    tocheck.lower()
    if tocheck[-1::-1] == tocheck:
        print(True)
    else:
        print(False)

palindromeOrNot()

# 9 To find Armstrong Number between two given number.

import copy 
def armstrongNumberOrNot():
    n = input("Enter a number to check wether it is an Armstrong Number or Not: ")
    try:
        n = int(n)
        n_copy = copy.copy(n)
    except ValueError:
        print("Enter a Integer Number.")
        armstrongNumberOrNot()
    
    # Extracting the digits of the number in a list
    digits = []
    for i in range(len(str(n))-1, -1, -1):
        quotient = n // (10 ** i)
        digits.append(quotient)
        n = n - (quotient * (10 ** i))

    # checking the actual logic
    lenOfNum = len(digits)

    armstrongSum = sum(x**lenOfNum for x in digits)
        
    if armstrongSum == n_copy:
        print(True)
    else:
        print(False)  
        print(armstrongSum)


armstrongNumberOrNot() 
    

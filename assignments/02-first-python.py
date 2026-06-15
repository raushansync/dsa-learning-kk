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
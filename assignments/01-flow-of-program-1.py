'''
[Video Link](https://youtu.be/lhELGQAV4gg)

## Create flowchart and pseudocode for the following:

1. Input a year and find whether it is a leap year or not.
2. Take two numbers and print the sum of both.
3. Take a number as input and print the multiplication table for it.
4. Take 2 numbers as inputs and find their HCF and LCM.
5. Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.

'''

# 1 soln.

def isLeapYear(year):
    ''' condition for a year to be a leap year:
    Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400 '''
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 400 == 0):
        return True
    else:
        return False    
    
print(isLeapYear(200)) # false


def isLeapYear(year):
    '''more compact form - chatgpt'''
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 2 soln. - Take two numbers and print the sum of both.

def sumOfBoth(a, b):
    return a + b

print(sumOfBoth(1, 2)) 

# 3 soln. - Take a number as input and print the multiplication table for it.

def multiplicationTable(num):
    for i in range(1, 11):
        print (f"{num} x {i} = {num * i}")

multiplicationTable(13)

# 4 soln. - Take 2 numbers as inputs and find their HCF and LCM.

def hcf(a, b):
    '''my version -  non optimised way - we are trying to find out the number equal to or less than the minumum number which divides both the given numbers.'''
    if a == 0 or b == 0:
        return max(a, b)
    else:
        result = min(a, b)
        while True:
            if a % result == 0 and b % result == 0:
                return result
            else:
                result -= 1
                
print(hcf(64,24))   

def gcd(a, b):
    '''Geeks for Geeks version'''
    # Everything divides 0
    if(a==0 or b==0):
        return max(a, b)
        
    # Find Minimum of a and b
    result = min(a, b)

    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    # Return gcd of a and b
    return result
print(hcf(64,24)) 
            

def hcf(a, b):
    '''Less efficient because it uses repeated subtraction instead of % (modulo).'''
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return max(a, b)
    elif a == b:
        return a
    else:
        if a > b:
            return hcf(a-b, b)
        else:
            return hcf(b-a, a)
        
print(hcf(64,24))


def hcf(a, b):
    '''efficient version using % instead of subtraction.'''
    a = abs(a)
    b = abs(b)
    min_num = min(a, b)
    max_num = max(a, b)
    return max_num if min_num == 0 else hcf(min_num, max_num % min_num)
print(hcf(64,24))


def hcf(a, b):
    '''chatgpt - you don't actually need min() and max()'''
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    return hcf(b, a % b)

print(hcf(64, 24))   # 8

# 5. Soln. -  Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.

def sumOfAll():
    total = 0
    while True:
        user_input = input("Enter a number here! ")
        if user_input.lower() == 'x':
            print(total)
            return
        else:
            try:
                user_input = int(user_input)
                total += user_input
            except ValueError:
                print("Enter a valid number")

sumOfAll()
        
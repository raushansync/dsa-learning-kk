# 9 To find Armstrong Number between two given number.

import copy 
def armstrongNumberOrNot(n):
    try:
        n = int(n)
        n_copy = copy.copy(n)
    except ValueError:
        print("Enter a Integer Number.")
        return False
    
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
        return True
    else:
        return False

def listOfarmstrongNumbersBetweenTwoNumbers(a, b):
    lis_of_armstrongNumbers = []
    try:
        a, b = int(a), int(b)
    except ValueError:
        print("Provide integers only.")
        return
    for i in range(a+1 , b):
        if armstrongNumberOrNot(i):
            lis_of_armstrongNumbers.append(i)
    print(lis_of_armstrongNumbers)



listOfarmstrongNumbersBetweenTwoNumbers(0, 1000)



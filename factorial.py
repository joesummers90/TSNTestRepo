def Factorial(number):
    # Set the total to the first number
    total = number
    while (number > 1):
        # subtract 1 from the number
        number = number - 1
        # multiply this to the total
        total = total * number
    return total

def Factorial2(number):
    # Set total to 1 to start the process
    total = 1
    while (number > 0):
        # Multiply the number to the total
        total = total * number
        # subtract 1
        number = number - 1
    return total

def Factorial3(number):
    total = number
    while (number > 0):
        number = number - 1
        if number > 0:
            total = total * number
    return total

def Factorial4(number):
    # Set the total to the first number
    total = number
    while (number > 1):
        # subtract 1 from the number
        number -= 1
        # multiply this to the total
        total *= number
    return total

def Factorial5(number):
    # Recursion example, each answer stored in stack before executing at the end when number = 1
    if number > 1:
        return number * Factorial5(number - 1)
    else:
        return number

print(Factorial(5))
print(Factorial2(5))
print(Factorial3(5))
print(Factorial4(5))
print(Factorial5(5))
# ======================{to sum of all number to givin rang}======================
"""
def calculate_sum():
    numbers = []  # Empty list to store the numbers
    total = 0

    ask = int(input("Enter the number of elements: "))
    for i in range(ask):
        choice = int(input(f"Enter number {i+1}: "))
        numbers.append(choice)

    for num in numbers:
     total += num  

    return f"The sum of the elements is {total}"

s = calculate_sum()
print(s)
"""


# ======================{to subtrac of all number to givin rang}======================
"""
def calculate_subtrac():
    numbers = []  # Empty list to store the numbers
    total = 0

    ask = int(input("Enter the number of elements: "))
    for i in range(ask):
        choice = int(input(f"Enter number {i+1}: "))
        numbers.append(choice)

    for num in numbers:
     total -= num  

    return f"The subtraction of the elements is {total}"

s = calculate_subtrac()
print(s)
"""

# ======================{to multiply of all number to givin rang}======================

"""
def multiply_function():
    numbers = []  # empty list to store the numbers
    total = 1   # total is 1 because we are multiplying 

    ask = int(input("Enter the number of elements: "))
    for i in range(ask):
        choice = int(input(f"Enter number {i+1}: "))
        numbers.append(choice)

    for num in numbers:
        total *= num  

    return f"The multiplication of the elements is {total}"

s = multiply_function()
print(s)
"""

# ======================{to divide of all number to givin rang}======================

"""
def divide_function():
    numbers = []  # Empty list to store the numbers

    ask = int(input("Enter the number of elements: "))
    for i in range(ask):
        choice = float(input(f"Enter number {i+1}: "))  # Input as float for division
        numbers.append(choice)

    # Initialize total with the first number in the list
    total = numbers[0]

    # Divide total by each subsequent number
    for num in numbers[1:]:
        if num == 0:
            return "Division by zero is not allowed."
        total /= num

    return f"The division of the elements is {total}"

s = divide_function()
print(s)
"""


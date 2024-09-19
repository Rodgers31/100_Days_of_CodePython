import art
def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator(sum):
    print(art.logo)
    num = input("What's the first number?: ")
    for symbol in operations:
        print(symbol)
    operator_value = input("Pick an operation: ")
    num2 = input("What's the next number?: ")
    num = float(num)
    num2 = float(num2)
    sum = (operations[f"{operator_value}"](num, num2))
    print(f"{num} {operator_value} {num2} = {sum}")
    output = sum
    return output

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
sum = 0
calculate = True

value = calculator(sum)
while calculate:
    continue_calc = input(f"Type 'y' to continue with {value}, or type 'n' to start a new calculation: ")
    if continue_calc == 'y':
        num = value
        print("+")
        print("-")
        print("*")
        print("/")
        operator_value = input("Pick an operation: ")
        num2 = input("What's the next number?: ")
        num = float(num)
        num2 = float(num2)
        value = (operations[f"{operator_value}"](num, num2))
        print(f"{num} {operator_value} {num2} = {value}")

    elif continue_calc == 'n':
        sum = 0
        calculator(sum)
    else:
        print('Invalid option')


import art
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


math_dictionary = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": div,
}

# print(math_dictionary["*"](4, 8))
print(art.logo)
def starting_operation(n1, n2, operator):
    # First operation in calculation
    if user_operator in math_dictionary:
        result = math_dictionary[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        return result

    else:
        print("Invalid Parameters")
        return None

first_number = float(input("What's your first number?: "))
for key in math_dictionary:
    print(key)
user_operator = input("Choose your operator: ")
second_number = float(input("What's your second number?: "))
result = starting_operation(n1= first_number, n2=second_number, operator=user_operator)

more_math = True
while more_math:

    finish = input('Type "y" to continue using this number or type "n" to start with new numbers.\n'
          'Alternatively type "done" if you are finished with the calculator. ').lower()

    if finish == "n":
        print("\n" * 20)
        print(art.logo)
        first_number = float(input("What's your first number?: "))
        for key in math_dictionary:
            print(key)
        user_operator = input("Choose your operator: ")
        second_number = float(input("What's your second number?: "))
        result = starting_operation(n1=first_number, n2=second_number, operator=user_operator)

    elif finish == "y":
        for key in math_dictionary:
            print(key)
        user_operator = input("Choose your operator: ")
        second_number = float(input("What's your second number?: "))
        first_number = result
        result = starting_operation(n1=first_number, n2=second_number,operator=user_operator)

    elif finish == "done":
        more_math = False


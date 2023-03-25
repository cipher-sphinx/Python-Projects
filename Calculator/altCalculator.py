# with errors handled


# Function to add two numbers
def add(x, y):
    return x + y


# Function to subtract two numbers
def subtract(x, y):
    return x - y


# Function to multiply two numbers
def multiply(x, y):
    return x * y


# Function to divide two numbers
def divide(x, y):
    return x / y


# Function to take input from the user
def get_input():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid Input. Please enter a number!")

    valid_choice = ["1", "2", "3", "4"]
    while True:

        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        choice = input("Enter choice(1/2/3/4): ")
        if choice in valid_choice:
            break
        else:
            print("Invalid choice! please try again.")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid Input. Please enter a number!")

    return choice, num1, num2


# Main function
while True:
    choice, num1, num2 = get_input()

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

    repeat = input("Do you want to perform another calculation? (Y/N): ")

    if repeat.lower() == 'n':
        break
    elif repeat.lower() == 'y':
        continue
    else:
        while True:
            invalid_choice = input("Invalid input. Do you want to quit? (Y/N): ")
            if invalid_choice.lower() == 'n':
                break
            elif invalid_choice.lower() == 'y':
                break
            else:
                continue

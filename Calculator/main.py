# A full-fledged calculator program in Python

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
   print("Select operation.")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")

   choice = input("Enter choice(1/2/3/4): ")

   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))

   return choice, num1, num2

# Main function
while True:
    choice, num1, num2 = get_input()

    if choice == '1':
        print(num1, "+", num2, "=", add(num1,num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1,num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1,num2))
    else:
        print("Invalid input")

    repeat = input("Do you want to perform another calculation? (Y/N): ")

    if repeat.lower() == 'n':
        break


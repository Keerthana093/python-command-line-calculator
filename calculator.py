import math
import time
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Clear screen function for better user experience
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Stylish animated banner
def show_banner():
    clear_screen()
    banner_text = " WELCOME TO PYTHON COMMAND-LINE CALCULATOR "
    print(Fore.CYAN + Style.BRIGHT + "=" * len(banner_text))
    for ch in banner_text:
        print(Fore.YELLOW + Style.BRIGHT + ch, end='', flush=True)
        time.sleep(0.03)
    print()
    print(Fore.CYAN + Style.BRIGHT + "=" * len(banner_text))
    print(Fore.GREEN + Style.BRIGHT + "\nMade using Python\n")
    time.sleep(0.8)

# Functions for basic operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return Fore.RED + " Error: Division by zero!"

# Operation menu
def show_menu():
    print(Fore.MAGENTA + "\n Choose an operation:")
    print(Fore.CYAN + "-" * 40)
    print(Fore.YELLOW + " 1  Addition (+)")
    print(Fore.YELLOW + " 2  Subtraction (-)")
    print(Fore.YELLOW + " 3  Multiplication (*)")
    print(Fore.YELLOW + " 4  Division (/)")
    print(Fore.YELLOW + " 5  Power (x^y)")
    print(Fore.YELLOW + " 6  Square Root (√)")
    print(Fore.YELLOW + " 7  Factorial (!)")
    print(Fore.YELLOW + " 8  Modulus (%)")
    print(Fore.RED + " 9  Exit ")
    print(Fore.CYAN + "-" * 40)

# Extra mathematical functions
def power(a, b): return a ** b
def sqrt(a): return math.sqrt(a)
def modulus(a, b): return a % b
def factorial(n): return math.factorial(n)

# Main calculator loop
def main():
    show_banner()
    while True:
        show_menu()
        choice = input(Fore.GREEN + Style.BRIGHT + "\nEnter your choice (1-9): ").strip()

        if choice == '9':
            print(Fore.YELLOW + "\n Thank you for using the calculator! Goodbye ")
            time.sleep(1)
            break

        # For operations needing two inputs
        if choice in ['1', '2', '3', '4', '5', '8']:
            try:
                num1 = float(input(Fore.CYAN + "Enter first number: "))
                num2 = float(input(Fore.CYAN + "Enter second number: "))
            except ValueError:
                print(Fore.RED + " Invalid input! Please enter valid numbers.")
                continue

            if choice == '1':
                result = add(num1, num2)
                symbol = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                symbol = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                symbol = "*"
            elif choice == '4':
                result = divide(num1, num2)
                symbol = "/"
            elif choice == '5':
                result = power(num1, num2)
                symbol = "^"
            elif choice == '8':
                result = modulus(num1, num2)
                symbol = "%"

            print(Fore.YELLOW + f"\n Result: {num1} {symbol} {num2} = {result}")

        # For operations needing one input
        elif choice == '6':
            try:
                num = float(input(Fore.CYAN + "Enter number: "))
                print(Fore.YELLOW + f"\n Result: √{num} = {sqrt(num)}")
            except ValueError:
                print(Fore.RED + " Invalid input!")
        elif choice == '7':
            try:
                num = int(input(Fore.CYAN + "Enter number: "))
                print(Fore.YELLOW + f"\n Result: {num}! = {factorial(num)}")
            except ValueError:
                print(Fore.RED + " Please enter an integer value!")

        else:
            print(Fore.RED + " Invalid choice! Please select from 1–9.")

        # Continue or exit
        again = input(Fore.MAGENTA + "\nDo you want to perform another calculation? (y/n): ").lower()

        if again == 'n':
            print(Fore.YELLOW + "\nThank you for using the calculator! Goodbye 😊")
            time.sleep(1)
            break
        elif again == 'y':
            print(Fore.GREEN + "\nContinuing your session...\n")
            time.sleep(0.8)
        else:
            print(Fore.RED + "Invalid input! Please enter 'y' or 'n'. Exiting by default.")
            break

# Run the program
if __name__ == "__main__":
    main()

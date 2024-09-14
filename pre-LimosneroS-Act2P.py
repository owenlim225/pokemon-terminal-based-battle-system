# Limosnero, Sherwin P.
# J2S
# Activity #2 P

import os

operator_lib = ["+", "-", "x", "/", "%", "^", "//"]


# Call if gusto pa ng user to try again
def again():
    while True:
        try:
            again = input("\n\n[C] Continue\t\t[X]Exit\n\n").lower()

            # Continue program
            if again == "c":
                os.system('cls') # clean terminal
                main()

            # Exit program
            elif again =="x":
                print("Thank you, please try agian.")
                os._exit(0)

        except ValueError:
            print("Invalid. Try again")


# Handle the calculation method
def calculate(num1, num2, operator):
    print()
    match operator:
        case "+":
            return f"{num1} + {num2} = {num1 + num2}"
        
        case "-":
            return f"{num1} - {num2} = {num1 - num2}"
        
        case "x":
            return f"{num1} x {num2} = {num1 * num2}"
        
        case "/":
            if num2 == 0:
                return "Error: Division by Zero"
            return f"{num1} / {num2} = {num1 / num2}"
        
        case "%":
            if num2 == 0:
                return "Error: Division by Zero"
            return f"{num1} % {num2} = {num1 % num2}"
        
        case "^":
            return f"{num1} ^ {num2} = {num1 ** num2}"
        
        case "//":
            if num2 == 0:
                return "Error: Division by Zero"
            return f"{num1} // {num2} = {num1 // num2}"
    print()
    print()

        

# Main function
def main():
    print("\tTerminal Calculator")

    while True: # Loop to get operator
        operator = input("""\nOperators:\n\n[+] Addition\t\t[-] Subtraction\n[x] Multiplication\t[/] Division\n[%] Modulus Division\t[^] Exponent\n[//] Floor Division\n\nOperator: """)

        if operator not in operator_lib:
            os.system('cls')
            print("Invalid, please try again.\n")
            continue
        else:
            break
    
    while True: # Loop to get nums
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
            break
        except ValueError:
            print("Invalid, please try again.\n")
                

    # Results
    result = calculate(num1, num2, operator)
    print(result)

    again()


        

if __name__ == "__main__":
    os.system('cls')
    main()
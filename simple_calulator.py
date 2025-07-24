number1 = int(input("Enter a First Number: "))
number2 = int(input("Enter a Second Number: "))

user_input = input("Enter a symbole (+,-,*,/,%): ")

if user_input == "+":
    total = number1 + number2
    print(f"Sum of {number1} + {number2} = {total}")

elif user_input == "-":
    Sub = number1 - number2
    print(f"Subtraction of {number1} - {number2} = {Sub}")

elif user_input == "*":
    Multi = number1 * number2
    print(f"Multiplication of {number1} * {number2} = {Multi}")

elif  user_input == "/":
    Div = number1 / number2
    print(f"Division of {number1} / {number2} = {Div}")


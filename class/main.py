import math

class Calculator:
    def main(self):
        print("Welcome to the calculator!")
        while True:
            print("Please enter a number or 'exit' to quit:")
            input_str = input()
            if input_str == "exit":
                break
            try:
                num1 = float(input_str)
                print("Please enter an operator (+, -, *, /, %, **, sqrt):")
                operator = input()
                if operator == "exit":
                    break
                if operator == "sqrt":
                    if num1 < 0:
                        print("Cannot calculate the square root of a negative number!")
                    else:
                        print(f"The square root of {num1} is {math.sqrt(num1)}")
                else:
                    print("Please enter another number:")
                    num2_str = input()
                    if num2_str == "exit":
                        break
                    num2 = float(num2_str)
                    if operator == "+":
                        print(num1 + num2)
                    elif operator == "-":
                        print(num1 - num2)
                    elif operator == "*":
                        print(num1 * num2)
                    elif operator == "/":
                        if num2 == 0:
                            print("Division by zero is not allowed!")
                        else:
                            print(num1 / num2)
                    elif operator == "%":
                        print(num1 % num2)
                    elif operator == "**":
                        print(num1 ** num2)
                    else:
                        print("Invalid operator!")
            except ValueError:
                print("Invalid input!")

if __name__ == '__main__':
    calculator = Calculator()
    calculator.main()

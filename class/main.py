class Calculator:
    def main(self):
        print("Welcome to the calculator!")
        while True:
            print("Please enter a number or an operator (+, -, *, /, %, **):")
            input_str = input()
            if input_str == "exit":
                break
            try:
                num1 = float(input_str)
                print("Please enter another number or an operator (+, -, *, /, %, **):")
                input_str = input()
                if input_str == "exit":
                    break
                if input_str == "**":
                    num2 = float(input_str)
                    print("Please enter the exponent:")
                    exp = float(input())
                    print(num1 ** exp)
                else:
                    num2 = float(input_str)
                    print("Please enter an operator (+, -, *, /, %, **):")
                    input_str = input()
                    if input_str == "exit":
                        break
                    if input_str == "+":
                        print(num1 + num2)
                    elif input_str == "-":
                        print(num1 - num2)
                    elif input_str == "*":
                        print(num1 * num2)
                    elif input_str == "/":
                        print(num1 / num2)
                    elif input_str == "%":
                        print(num1 % num2)
                    elif input_str == "**":
                        print(num1 ** num2)
                    else:
                        print("Invalid operator!")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    calculator = Calculator()
    calculator.main()
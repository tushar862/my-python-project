def arithmetic_operations():
    print("Arithmetic Operations: +, -, *, /")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    num2 = float(input("Enter second number: "))
    if operator == '+':
        print(f"Result: {num1 + num2}")
    elif operator == '-':
        print(f"Result: {num1 - num2}")
    elif operator == '*':
        print(f"Result: {num1 * num2}")
    elif operator == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operator!")

def logical_operations():
    print("Logical Operations: and, or, not")
    val1 = input("Enter first boolean value (True/False): ").strip().capitalize()
    operator = input("Enter operator: ").strip()
    if operator == 'not':
        print(f"Result: {not eval(val1)}")
    else:
        val2 = input("Enter second boolean value (True/False): ").strip().capitalize()
        if operator == 'and':
            print(f"Result: {eval(val1) and eval(val2)}")
        elif operator == 'or':
            print(f"Result: {eval(val1) or eval(val2)}")
        else:
            print("Invalid operator!")

def comparative_operations():
    print("Comparative Operations: >, <, ==, !=, >=, <=")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    num2 = float(input("Enter second number: "))
    if operator == '>':
        print(f"Result: {num1 > num2}")
    elif operator == '<':
        print(f"Result: {num1 < num2}")
    elif operator == '==':
        print(f"Result: {num1 == num2}")
    elif operator == '!=':
        print(f"Result: {num1 != num2}")
    elif operator == '>=':
        print(f"Result: {num1 >= num2}")
    elif operator == '<=':
        print(f"Result: {num1 <= num2}")
    else:
        print("Invalid operator!")

def main():
    print("Select the type of operation:")
    print("1. Arithmetic Operations")
    print("2. Logical Operations")
    print("3. Comparative Operations")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        arithmetic_operations()
    elif choice == '2':
        logical_operations()
    elif choice == '3':
        comparative_operations()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

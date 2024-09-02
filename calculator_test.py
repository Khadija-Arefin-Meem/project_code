import calculator_case as cal
while True:
    print("option 1: Add")
    print("option 2: Subtraction")
    print("option 3: Multiplication")
    print("option 4: Division")
    op=input("Enter option: ")
    if op not in ['1', '2', '3', '4']:
        print("Invalid option! Please select a valid option.")
        break
    a= int(input("Enter the first number:"))
    b=  int(input("Enter the second number:"))
    result = cal.calculator(op, a, b)
    print(f'The result of the operation is: {result}')


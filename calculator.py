print('Welcome to the calculator program.')
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print('''
 _____________________
|  _________________  |
| | JO           0. | | 
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

          ''')
    
    print('''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
          
''')
    should_continue = True
    num1 = float(input("What's the first number?: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        progress = input(f"Type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation: ").lower()

        if progress == "yes":
            num1 = answer
        else:        
            should_continue = False
            print("\n" * 100)
            calculator()
calculator()
   
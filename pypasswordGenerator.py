#Password Generator Project
import random
#lists of characters to be used in password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#greeting
print("Welcome to the PyPassword Generator!")
choose_level = input("Do you want hard or easy level password? " 
            "Type 'easy' or 'hard': " ).lower()
if choose_level != "easy" and choose_level != "hard":
    print("Invalid input. Please choose either 'easy' or 'hard'.")
elif choose_level == "easy":
        #variables to store user input
    number_of_letters = int(input("How many letters would you like in your password?\n"))
    number_of_symbols = int(input("How many symbols would you like?\n"))
    number_of_numbers = int(input("How many numbers would you like?\n"))
    #empty string to store the generated password

    print(f"You have chosen to have {number_of_letters} letters, {number_of_symbols} symbols and {number_of_numbers} numbers in your password.")
    password = ""
    #Easy Level - Order not randomised:
    #generate random letters
    for char in range(1, number_of_letters + 1):
        password += random.choice(letters)      
    #generate random symbols
    for char in range(1, number_of_symbols + 1):
        password += random.choice(symbols)      
    #generate random numbers
    for char in range(1, number_of_numbers + 1):
        password += random.choice(numbers)  
    print(f"Your password is: {password}")    
else:
        #variables to store user input
    number_of_letters = int(input("How many letters would you like in your password?\n"))
    number_of_symbols = int(input("How many symbols would you like?\n"))
    number_of_numbers = int(input("How many numbers would you like?\n"))
    #empty string to store the generated password

    print(f"You have chosen to have {number_of_letters} letters, {number_of_symbols} symbols and {number_of_numbers} numbers in your password.")
    #Hard Level - Order of characters randomised:
    password_list =[]
    #generate random letters
    for char in range(1, number_of_letters + 1):
        password_list.append(random.choice(letters))    
    #generate random symbols
    for char in range(1, number_of_symbols + 1):
        password_list.append(random.choice(symbols))    
    #generate random numbers        
    for char in range(1, number_of_numbers + 1):
        password_list.append(random.choice(numbers))
    #shuffle the list to randomise the order of characters
    random.shuffle(password_list)
    print(password_list)
    #convert list to stringpassword = ""
    password = ""
    for char in password_list:
        password += char
    print(f"Your password is: {password}")
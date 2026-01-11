#RollercoasterHeightCheck
print("Welcome to the Rollercoaster!")

#accepting height input from user
height = int(input("Please enter your height in cm: "))

#this condition checks the height for ride eligibility
if height >= 120 :
    print("You are tall enough to ride the rollercoaster!")

    #this condition checks the age for ticket pricing
    #accepting age input from user
    age = int(input("Please enter your age: "))
    if age <= 12:
        print("Your ticket price is $5.")
    elif age <= 18:
        print("Your ticket price is $7.")
    else:
        print("Your ticket price is $12.")
else:
    print("Sorry, you need to be at least 120 cm tall to ride the rollercoaster.")

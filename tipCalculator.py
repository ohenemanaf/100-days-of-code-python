#Tip Calculator
print("Welcome to The TIp Calculator")

#Accepting input from the user
bill = int(input("What's your Total Bill? \n"))

tip = int(input("What percent willyou tip? 10, 12, 15 \n"))

shareAmong = int(input("How many people are to pay the total bill? \n"))

#formula to calculate the bill
total_bill = bill + (tip/100)*bill

eachPayment = total_bill/shareAmong

#This outputs the total bill
print(f"Total bill = {total_bill}")

#This outputs the bill each person will pay
print(f"Each person should pay ${eachPayment}")
 


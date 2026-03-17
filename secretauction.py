#secret auction
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to the secret auction program.")
bids = {}
def bid_question():
    
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: $ "))
    bids[name] = amount
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "yes":
        print("\n" * 100)
        bid_question()
    else:
        highest_bidder = ""
        highest_amount = 0
        for bidder in bids:
            if bids[bidder] > highest_amount:
                highest_amount = bids[bidder]
                highest_bidder = bidder
        print(f"The winner is {highest_bidder} with a bid of ${highest_amount}.")
bid_question()

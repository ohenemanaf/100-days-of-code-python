import random

rock = '''
    _______
---'   ____)
       (_____)
       (_____)
       (____)
---.__(___) 

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)   

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
choice = int(input("Welcome to Rock, Paper, Scissors!\n"
                   "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if choice >=3 or choice < 0:
    print("Invalid choice. Please choose 0, 1, or 2.")
else:
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)
    else:
        print("Invalid choice. Please choose 0, 1, or 2.")

    computer_choice = random.randint(0, 2)

    if computer_choice == 0:
        print("Computer chose rock")
        print(rock)
    elif computer_choice == 1:
        print("Computer chose paper")
        print(paper)
    elif computer_choice == 2:
        print("Computer chose scissors")
        print(scissors)

    # Determine the winner
    if choice == computer_choice:
        print("It's a draw!")
    elif choice == 0 and computer_choice == 2:
        print("You win!")
    elif choice == 1 and computer_choice == 0:
        print("You win!")
    elif choice == 2 and computer_choice == 1:
        print("You win!")

    else:
        print("You lose!")

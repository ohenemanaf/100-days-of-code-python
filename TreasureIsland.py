print('''
*****************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
      
*****************************************************************
      ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input("You're at a crossroad. "
                  "Where do you want to go? "
                  "Type 'left' or 'right': ")

if crossroad == "left" or crossroad == "Left" or crossroad == "LEFT":
    lake = input("You've reached a lake."
                 "There is an island in the middle of the lake."
                 "Do you want to swim or wait? Type 'swim' or 'wait': ")
    
    if lake == "wait" or lake == "Wait" or lake == "WAIT":
        door = input("You've arrived at the island. "
                     "There is a house with three doors. "
                     "Which door do you choose? "
                     "Type 'red', 'blue', or 'yellow': ")
        if door == "yellow" or door == "Yellow" or door == "YELLOW":
            print("You found the treasure!🏆  You Win!🥇🎉")

        elif door == "red" or door == "Red" or door == "RED":
            print("It's a room full of fire. Game Over.")

        elif door == "blue" or door == "Blue" or door == "BLUE":
            print("You enter a room of beasts. Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")



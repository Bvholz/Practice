print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
name = input("Please enter your name:")
print("Welcome to Treasure Island", name + ".")
print("Your mission is to find the treasure.")

#First Direction
choice1 = input("You see two roads ahead. One to the left and one to the right. Which do you choose?")
if choice1 == "left":
    print("You fall into a hole. Game Over.")
else:
    choice2 = input("You follow the road and come to a dock. Do you swim to the adjacent landmass or wait for the next boat? Enter swim or wait.")
    if choice2 == "swim":
        print("You were eaten by a Kraken. Game Over.")
    else:
        choice3 = input("The boat arrives 5 minutes later and brings you to a castle. You see 3 doors. One red, one yellow, and one blue. Which do you choose?")

        if choice3 == "yellow":
            print("Congratulations, you found the treasure.")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game Over.")
        else:
            print("You were burned by fire. Game Over.")
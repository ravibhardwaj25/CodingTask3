import random

print("*****Welcome to Rock, Paper and Scissor game there are 5 chances available to play this game*****")
print()

# Initial scores of user and computer are 0 and number of ties is also equal to 0
user_score = 0
comp_score = 0
ties = 0
# User enter its name first
name = input("Enter your name here: ")
print("""
Winning Rules:
1. Rock vs Scissor --> Rock Wins
2. Scissor vs Paper --> Scissor Wins
3. Paper vs Rock --> Paper Wins""")
print()
i=0
while i<5:
    # Now user input its choice from the given choices
    print("""
    Choices are:
    Choose 1 for Rock
    Choose 2 for Paper
    Choose 3 for Scissor
    """)
    print()
    choice= int(input("enter your choices from 1-3: "))
    print()
    while choice > 3 or choice < 1:
        choice= int(input("enter valid input from 1-3: "))
    # Set the variable so that computer also understand that 1 means Rock, 2 means Paper and 3 means Scissor
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissor"

    print(name," choice is ",user_choice)
    print("Now it is Computer's turn")

    # computer takes random number between 1-3 by using random module which is imported at starting phase
    computer = random.randint(1,3)
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissor"

    print(" The computer's choice is", comp_choice)

    if((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("Paper wins")
        result = "Paper"
    elif (((user_choice == "Scissor" and comp_choice == "Rock")) or (user_choice == "Rock" and comp_choice == "Scissor")):
        print("Rock wins")
        result = "Rock"
    elif(user_choice == comp_choice):
        print("It's  a Draw")
        result = "Tie"
    else:
        print("Scissor Win")
        result = "Scissor"

    if result == "Tie":
        ties +=1
    elif result == user_choice:
        print(name," wins")
        user_score +=1
    else:
        print("computer wins")
        comp_score +=1

    print("Scores are")
    print(name + "'s score is", user_score)
    print("computer's score is",comp_score)
    print("Number of Draw in match are",ties)

    i +=1

if user_score > comp_score:
    print(name + " wins finally")
elif user_score == comp_score:
    print("It is a Draw finally")
else:
    print("computer wins finally")

with open("highscoring.txt","r") as f:
    highscore=int(f.read())
if user_score>highscore:
    print(name+ " have just broken the high score!")
    with open("highscoring.txt","w") as f:
        f.write(str(user_score))                  

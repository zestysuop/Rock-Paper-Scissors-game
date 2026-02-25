""" 
workflow of project:
1- Input from user(Rock, Paper, Scissors)
2- Computer choice(computer will choose randomly not conditionally)
3- Result print at the end of each round

cases:
A: ROCK
Rock-Rock = tie
Rock-Paper = Paper wins
Rock-Scissors = Rock wins

B: PAPER
Paper-Rock = Paper wins
Paper-Paper = tie
Paper-Scissors = Scissors wins 

C: SCISSORS
Scissors-Rock = Rock wins
Scissors-Paper = Scissors
Scissors-Scissors = tie



"""

import random
item_list = ["Rock", "Paper", "Scissors"]
user_choice = input("Enter your move = Rock, Paper, Scissors = ")
computer_choice = random.choice(item_list)
print(f"User choice = {user_choice}, Computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie")
elif user_choice == "Rock" :
    if computer_choice == "Paper":
        print("Paper wins!")
    else:
        print("Rock smashes Scissors! You win!")  
elif user_choice == "Paper":
    if computer_choice == "Scissors":
        print("Scissors cuts Paper! Computer wins!")
    else:
        print("Paper covers Rock! You win!")  
elif user_choice == "Scissors":   
    if computer_choice == "Rock":
        print("Rock smashes Scissors! Computer wins!")
    else:
        print("Scissors cuts Paper! You win!")                 
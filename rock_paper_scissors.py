# -*- coding: utf-8 -*-
"""
rock - paper - scissors 
@author: Amol
"""
import random

while True:
    continue_or_not = input("do you want to play?")

    if continue_or_not in "NOno":
        break 
    user_choice = int(input("please give in input of rock(0), paper(1) or scissors(2) : "))
    if user_choice not in [0,1,2]:
        print("please give valid input" )
    else:
        print(option[computer_choice],"(computer)  vs  (user)",option[user_choice])
        computer_choice = random.randint(0,2)
        computer = computer_choice
        option= ["rock","paper","scissors"]
        if computer == user_choice:
            print(" DRAW ")
        elif (option[computer] == "rock" and option[user_choice] == "paper"):
            print(" PLAYER WINS ")
        elif (option[computer] == "rock" and option[user_choice] == "scissors"):
            print(" COMPUTER WINS ")
        elif (option[computer] == "paper" and option[user_choice] == "scissors"):
            print(" PLAYER WINS ")
        elif option[computer] == "paper" and option[user_choice] == "rock":
            print(" COMPUTER WINS ")
        elif option[computer] == "scissors" and option[user_choice] == "rock":
            print(" PLAYER WINS ")
        elif option[computer] == "scissors" and option[user_choice] == "paper":
            print(" COMPUTER WINS ")
        print(computer,computer_choice)
    
    

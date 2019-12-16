# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:23:29 2019

@author: Amol
"""
import random 

def user_input():
    while True: 
        x = int(input("please give your input (rock = 0, paper = 1, scissors = 2) :  "))
        if x in [0,1,2]:
            return x



def comp_choice():
    x = random.randint(0,2)
    return x 

def winner(x,y):# x- user
    #lyst = ["rock","paper","scissors"]
    
    printer(x,y)
    if x == y:
        return ("draw")
    if x == 0 and y == 1:
        return ("computer wins")
    if x == 0 and y == 2:
        return ("player wins") 
    if x == 1 and y == 2:
        return ("computer wins")
    if x == 1 and y == 0:
        return ("player wins") 
    if x == 2 and y == 0:
        return ("computer wins")
    if x == 2 and y == 1:
        return ("player wins") 

def printer(x,y):
    lyst= ["rock","paper","scissor"]
    print ("player chose : ",lyst[x])
    print ("computer chose : ",lyst[y])

def main():
    winner_count = 0 
    user_win = 0 
    comp_win = 0
    for i in range (5):
        x = user_input()
        y = comp_choice()
        print(winner(x,y))
        if winner(x,y) == "computer wins": 
            comp_win += 1
        if winner(x,y) == "player wins": 
            user_win += 1
    print(user_win)
    print(comp_win)

        
if __name__ == "__main__":
    main()
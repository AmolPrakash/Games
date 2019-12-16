# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:16:36 2019

@author: Amol
"""
import random 
class Rock_paper_scissor:
    def __init__(self):
        self.user = 0  
        self.computer = 0 
        
    def printer(self):
        lyst= ["rock","paper","scissor"]
        print("user is : ", lyst[self.user])
        print("computer is : ", lyst[self.computer])
    
    def set_user_input(self):
        switch = True
        while switch: 
            temp = int(input("0 - rock, 1 - paper, 2 - scissors :"))
            if temp in [0,1,2]:
                self.user = temp
                switch = False
            else:
                print (" Please choose one of the options ")
                
    
    def set_computer_input(self):
        self.computer = random.randint(0,2)
        
    def get_user_input(self):
        return self.user
    
    def get_winner(self):
        return (self.winner)
    
    def winner(self):
        self.printer()
        if self.user == self.computer:
            self.winner = "draw"
        if self.user == 0 and self.computer == 1:
            self.winner = ("computer wins")
        if self.user == 0 and self.computer == 2:
            self.winner = ("player wins")   
        if self.user == 1 and self.computer == 2:
            self.winner = ("computer wins")
        if self.user == 1 and self.computer == 0:
            self.winner = ("player wins") 
        if self.user == 2 and self.computer == 0:
            self.winner = ("computer wins")
        if self.user == 2 and self.computer == 1:
            self.winner = ("player wins")
for i in range(10):
    
    amol = Rock_paper_scissor()
    amol.set_user_input()
    amol.set_computer_input()
    amol.winner()
    print(amol.get_winner())

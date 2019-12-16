from random import *

x = randint(0,1)

if x == 0:
    player1 ='X'
    player2 ='O'

else:
    player2 = 'X'
    player1= 'O'

x = randint(0,1)

if x == :
    start = 'player1'
else:
    start = 'player2'

print ("Welcome to tic tac toe")

print ("Player1 plays with ",player1)

print("Player2 plays with ",player2)

print(start, "Starts")

board = [ i+1 for i in range(9)]

#print board

print("Beging Board State")

foor i in range (len(board)):
    print(board[i], end= '  |  ')
    if (i==2 or i == 5 or i==8):
        print ("\n")
        print("---------------------")
        

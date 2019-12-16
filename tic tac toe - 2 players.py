from random import *

x = randint(0,1)

if x == 0:
    player1= 'X'
    player2= '0'
else:
    player2= 'X'
    player1= '0'

x = randint(0,1)

if x == 0:
    start='player1'
else:
    start='player2'


print ("Welcome to tic tac toe ")

print ("Player1 plays with ", player1)

print ("Player2 plays with ",player2)


print (start, " Starts")

board = [ i+1  for i in range(9) ]

# print board

print ("Begin Board State")

for i in range (len(board)):
    print (board[i], end=' | ')
    if (i==2 or i == 5 or i==8):
        print ("\n")
        print("--------------")


#print ("\n")


if start=='player1':
    current =  'player1'
    for i in range(9):
        if (current == 'player1'):
             print ("Player1 turn ----")
             move=int(input("Choose a place player1 : "))
             board[move-1]=player1
             current= 'player2'
        elif(current == 'player2'):
             print ("player2 turn ---")
             move=int(input("Choose a place player2 : "))
             #x = randint(0,8)
             #while (board[x] == 'X' or board[x] == '0'):
                 #x = randint(0,8)
             board[move-1] = player2
             current = 'player1'
             
        print ("Board State")

        for i in range (len(board)):
             print (board[i], end=' | ')
             if (i==2 or i == 5 or i ==8):
                print ("\n")
                print("--------------")
             

if start=='player2':
    current = 'player2'
    for i in range(9):
        if (current == 'player1'):
             print ("Player1 turn ----")
             move=int(input("Choose a place player1 : "))
             board[move-1]=player1
             current= 'player2'
        elif(current == 'player2'):
             print ("player2 turn ---")
             move=int(input("Choose a place player2 : "))
             #x = randint(0,8)
             #while (board[x] == 'X' or board[x] == '0'):
                 #x = randint(0,8)
             board[move-1] = player2
             current = 'player1'
             
        print ("Board State")

        for i in range (len(board)):
             print (board[i], end=' | ')
             if (i==2 or i == 5 or i == 8):
                print ("\n")
                print("--------------")


#print board

print ("Final Board State")

                     
for i in range (len(board)):
    print (board[i], end=' | ')
    if (i==2 or i == 5 or i==8):
        print ("\n")
        print("--------------")
         
#check winner

winner = False

#check rows
for i in range (0,len(board),3):
    if (board[i]==board[i+1] and board[i+1]==board[i+2]):
        print ("Winner is ", board[i])
        winner = True

#check columns
for i in range (0,3):
    if (board[i]==board[i+3] and board[i+3]==board[i+6]):
        print ("Winner is ", board[i])
        winner = True

#check diagonal

if (board[0] == board[4] and board[4] == board[8]):
    print ("Winner is ", board[0])
    winner = True

if winner == False:
    print ("It's a tie")




         
    

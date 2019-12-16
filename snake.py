# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:58:31 2019

@author: Amol
"""
import turtle
import time
import random

#this acts like the difficulty level for the game and will keep reducing as the game proceeds
delay = 0.1 


score = 0 
high_score = 0 


body_parts = [] 

#for screen 
window = turtle.Screen()
window.title("SNAKE")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0)

#for the head of the turtle 
head = turtle.Turtle()
head.speed(10)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'
body_parts.append(head)

#food for snake 
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
head.goto(0,100)

# to show score 
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color('white')
pen.hideturtle()
pen.goto(0,-275)
pen.write("score: {} High Score: {}".format(score,high_score),align = 'center',font =('Arial',18,"normal"))

#movement for the snake 
def move():
    if head.direction =='up':
        head.sety(head.ycor()+20)
    if head.direction =='down':
        head.sety(head.ycor()-20)
    if head.direction =='right':
        head.setx(head.xcor()+20)
    if head.direction =='left':
        head.setx(head.xcor()-20)

def go_up():
    if head.direction != 'down': 
        head.direction = 'up'
def go_down():
    if head.direction != 'up': 
        head.direction = 'down'
def go_left():
    if head.direction != 'right': 
        head.direction = 'left'
def go_right():
    if head.direction != 'left': 
        head.direction = 'right'
        
def endGame():
    head.direction = 'stop'
    #window.bye()

    
window.listen()
window.onkey(go_up,"Up")
window.onkey(go_down,"Down")
window.onkey(go_left,"Left")
window.onkey(go_right,"Right")
window.onkey(endGame,"Escape")

while True:
    window.update()
    
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    #when the snake gets food 
    if head.distance(food) < 20:
        food.goto(random.randint(-289,289),random.randint(-289,289))
        body = turtle.Turtle()
        body.speed(10)
        body.shape('square')
        body.color('yellow')
        body.penup()
        body_parts.append(body)   
        score += 10
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("score: {} High Score: {}".format(score,high_score),align = 'center',font =('Arial',18,"normal"))

    #this is so that the tail of the snake follows the head    
    for part in range(len(body_parts)-1,0,-1):
        body_parts[part].goto(body_parts[part-1].xcor(),body_parts[part-1].ycor())
        
    if body_parts:
        body_parts[0].goto(head.xcor(),head.ycor())
    move()
    
    
    #if it collides with itself 
    for parts in body_parts:
        if parts.distance(head)<20:
            time.sleep(1)
            delay = 0.1
            head.goto(0,0)
            head.direction = 'stop'
            for body in body_parts:
                body.goto(1000,1000)
            body_parts.clear()
            score = 0
            pen.clear()
            pen.write("score: {} High Score: {}".format(score,high_score),align = 'center',font =('Arial',18,"normal"))
            
    time.sleep(delay)
    if delay >0.01:
        delay -=0.00001
window.clear()
window.mainloop()

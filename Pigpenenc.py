#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Author - Bl4cKc34sEr 


from turtle import Turtle
import turtle

AllLetters   = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NoDots       = ["a","b","c","d","e","f","g","h","i"]
WithDots     = ["j","k","l","m","n","o","p","q","r","w","y","z","x"]
Lefts        = ["b","c","e","f","h","i","k","l","n","o","q","r"]
Rights       = ["a","b","d","e","g","h","j","k","m","n","p","q"]
Bottoms      = ["a","b","c","d","e","f","j","k","l","m","n","o"]
Tops         = ["d","e","f","g","h","i","m","n","o","p","q","r"]
Diagonal     = ["s","t","u","v"]
DiagonalDots = ["w","x","y","z"]

fontSize = 0.8

def InitialiseTurtle(t):
    t.speed(0)
    t.hideturtle()
    t.pensize(3)
    t.color('black')

def PenGoto(loc,t):
    t.penup()
    t.goto(loc)
    t.pendown()

def Left(locx,locy,t):
    PenGoto((locx,locy),t)
    t.setheading(90)
    t.forward(40*fontSize)

def Right(locx,locy,t):
    PenGoto((locx+40*fontSize,locy),t)
    t.setheading(90)
    t.forward(40*fontSize)

def Bottom(locx,locy,t):
    PenGoto((locx,locy),t)
    t.setheading(0)
    t.forward(40*fontSize)

def Top(locx,locy,t):
    PenGoto((locx,locy+40*fontSize),t)
    t.setheading(0)
    t.forward(40*fontSize)

def LeftD(locx,locy,t):
    PenGoto((locx,locy+20*fontSize),t)
    t.setheading(90-63.43)
    t.forward(44.72*fontSize)
    PenGoto((locx,locy+20*fontSize),t)
    t.setheading(-90+63.43)
    t.forward(44.72*fontSize)

def RightD(locx,locy,t):
    PenGoto((locx+40*fontSize,locy+20*fontSize),t)
    t.setheading(90+63.43)
    t.forward(44.72*fontSize)
    PenGoto((locx+40*fontSize,locy+20*fontSize),t)
    t.setheading(-90-63.43)
    t.forward(44.72*fontSize)

def BottomD(locx,locy,t):
    PenGoto((locx+20*fontSize,locy),t)
    t.setheading(63.43)
    t.forward(44.72*fontSize)
    PenGoto((locx+20*fontSize,locy),t)
    t.setheading(116.57)
    t.forward(44.72*fontSize)

def TopD(locx,locy,t):
    PenGoto((locx+20*fontSize,locy+40*fontSize),t)
    t.setheading(-63.43)
    t.forward(44.72*fontSize)
    PenGoto((locx+20*fontSize,locy+40*fontSize),t)
    t.setheading(180+63.43)
    t.forward(44.72*fontSize)

def Square(mode,locx,locy):
    if "left" in mode:
        Left(locx,locy,draw)
    if "right" in mode:
        Right(locx,locy,draw)
    if "bottom" in mode:
        Bottom(locx,locy,draw)
    if "top" in mode:
        Top(locx,locy,draw)
    if "deft" in mode:
        LeftD(locx,locy,draw)
    if "dot" in mode:
        BottomD(locx,locy,draw)
    if "dop" in mode:
        TopD(locx,locy,draw)
    if "dight" in mode:
        RightD(locx,locy,draw)

def Circle(locx,locy,t):
    temp = t.pensize()
    PenGoto((locx+20*fontSize,locy+20*fontSize),draw)
    draw.pensize(10*fontSize)
    draw.forward(0.01)
    draw.pensize(temp)

draw = Turtle()
InitialiseTurtle(draw)

x = -250
y = 200

PlainText = input("Enter the message to be displayed: ")
for i in PlainText:
    try:
        i = i.lower()
    except:
        None
    mode = ""
    if i in WithDots:
        Circle(x,y,draw)
    if i in Lefts:
        mode+="left"
    if i in Rights:
        mode+="right"
    if i in Bottoms:
        mode+="bottom"
    if i in Tops:
        mode+="top"
    if i in ["s","w"]:
        mode+="dot"
    if i in ["v","z"]:
        mode+="dop"
    if i in ["t","x"]:
        mode+="dight"
    if i in ["u","y"]:
        mode+="deft"
    Square(mode,x,y)

    x += 45*fontSize
    if x >= 250:
        x = -250
        y -= 45*fontSize


# In[]:

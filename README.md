# Pig-Enc

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/]
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)]
[![GitHub followers](https://img.shields.io/github/followers/Bl4cKc34sEr.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/Bl4cKc34sEr?tab=followers)

Pig-Enc is Pigpen Cipher Encoding Script writen in Python Programming Language.
The library used is TURTLE library.

INTRODUCTION TO TURTLE:
The turtle module is an extended reimplementation of the same-named module from the Python standard distribution up to version Python 2.5.

It tries to keep the merits of the old turtle module and to be (nearly) 100% compatible with it. This means in the first place to enable the learning programmer to use all the commands, classes and methods interactively when using the module from within IDLE run with the -n switch.

The turtle module provides turtle graphics primitives, in both object-oriented and procedure-oriented ways. Because it uses tkinter for the underlying graphics, it needs a version of Python installed with Tk support.

The object-oriented interface uses essentially two+two classes:

The TurtleScreen class defines graphics windows as a playground for the drawing turtles. Its constructor needs a tkinter.Canvas or a ScrolledCanvas as argument. It should be used when turtle is used as part of some application.

The function Screen() returns a singleton object of a TurtleScreen subclass. This function should be used when turtle is used as a standalone tool for doing graphics. As a singleton object, inheriting from its class is not possible.

All methods of TurtleScreen/Screen also exist as functions, i.e. as part of the procedure-oriented interface.

RawTurtle (alias: RawPen) defines Turtle objects which draw on a TurtleScreen. Its constructor needs a Canvas, ScrolledCanvas or TurtleScreen as argument, so the RawTurtle objects know where to draw.

Derived from RawTurtle is the subclass Turtle (alias: Pen), which draws on “the” Screen instance which is automatically created, if not already present.

All methods of RawTurtle/Turtle also exist as functions, i.e. part of the procedure-oriented interface.

The procedural interface provides functions which are derived from the methods of the classes Screen and Turtle. They have the same names as the corresponding methods. A screen object is automatically created whenever a function derived from a Screen method is called. An (unnamed) turtle object is automatically created whenever any of the functions derived from a Turtle method is called.

To use multiple turtles on a screen one has to use the object-oriented interface.

METHODS IN TURTLE:

For Turtle motion:-
Move and draw
  forward() | fd()
  backward() | bk() | back()
  right() | rt()
  left() | lt()
  goto() | setpos() | setposition()
  setx()
  sety()
  setheading() | seth()
  home()
  circle()
  dot()
  stamp()
  clearstamp()
  clearstamps()
  undo()
  speed()
Tell Turtle’s state
  position() | pos()
  towards()
  xcor()
  ycor()
  heading()
  distance()
Setting and measurement
  degrees()
  radians()

Pen control:
Drawing state:-
  pendown() | pd() | down()
  penup() | pu() | up()
  pensize() | width()
  pen()
  isdown()
Color control
  color()
  pencolor()
  fillcolor()
  Filling
  filling()
  begin_fill()
  end_fill()
More drawing control
  reset()
  clear()
  write()
Turtle state
Visibility
  showturtle() | st()
  hideturtle() | ht()
  isvisible()
Appearance
  shape()
  resizemode()
  shapesize() | turtlesize()
  shearfactor()
  settiltangle()
  tiltangle()
  tilt()
  shapetransform()
  get_shapepoly()
Using events
  onclick()
  onrelease()
  ondrag()
Special Turtle methods
  begin_poly()
  end_poly()
  get_poly()
  clone()
  getturtle() | getpen()
  getscreen()
  setundobuffer()
  undobufferentries()

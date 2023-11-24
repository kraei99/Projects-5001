"""
CS5001
Kayser Raei
Homework 3
Fall 2023
"""

import turtle
from PositionService import get_position_x, get_position_y, set_position_x, set_position_y, set_visible, is_visible

pen = turtle.Turtle()
pen.hideturtle()

def setup():
     # Set up the turtle window size and background picture
    turtle.setup(970, 635)
    turtle.bgpic("shape_window.png")

#Draw a circle with specified parameters.
def draw(x, y, rad=80, color="green"):
    pen.penup()
    pen.goto(x, y - rad)
    pen.pendown()
    pen.color(color)
    pen.circle(rad)
    set_visible(True)

def click(x, y):
    # Check if the circle is currently visible
    if is_visible():
        if abs(x - get_position_x()) < 80 and abs(y - get_position_y()) < 80:
            pen.clear() # Clear the circle if clicked inside it
            set_visible(False)
    else:
        # If no visible circle, set the new circle's position and draw a new circle
        set_position_x(x)
        set_position_y(y)
        draw(x, y)

def start():
    setup()
    draw(0, 0) #Draw initial circle
    turtle.onscreenclick(click) #connect the click function to mouse clicks
    turtle.mainloop()

if __name__ == "__main__":
    start()
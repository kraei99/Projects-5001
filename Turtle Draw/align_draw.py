'''
CS5001
Fall 2023
Kayser Raei
Homework 2
'''

# Import the turtle graphics library
import turtle

t = turtle.Turtle()

# A Function draw a blue square (problem 1)
def square():
    '''Drawing a blue square with side length 80 units, located at (-40, 40).'''

    t.penup()
    t.goto(-40,40)
    t.pencolor("blue")
    t.pendown()

    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)

# A Function draw a red circle (problem 2)
def circle():
    '''Drawing a red circle with a radius of 40 units, center at (0, -40).'''

    t.penup()
    t.goto(0, -40)
    t.right(90)
    t.pencolor("red")
    t.pendown()
    
    # Draw the circle
    t.circle(40)


# A Function drawing a new square (filled purple) with given coordinates (user)
def new_square(square_x, square_y):
    '''Drawing a square, filled purple, side length 80 units after given coordinates.'''

    t.penup()
    t.goto(square_x,square_y)
    t.pencolor("blue")
    t.begin_fill()
    t.fillcolor("purple")
    t.pendown()

    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)

    t.end_fill()

# A Function drawing a new circle (filled green) with given coordinates (user)
def new_circle(circle_x, circle_y):
    '''Drawing a circle, filled green, radius of 40 units after given coordinates.'''

    t.penup()
    t.goto(circle_x, circle_y)
    t.right(90)
    t.pencolor("red")
    t.begin_fill()
    t.fillcolor("green")
    t.pendown()
    
    # Draw the circle
    t.circle(40)
    t.end_fill()


def main():
    
    # Draw the first square and circle (question 2)
    square ()
    circle ()

    # Clear previous drawings before drawing the new shapes
    t.clear()

    # Getting coordinates from user for the new square
    square_x = float(input("enter the x coordinate for the square: "))
    square_y = float(input("enter the y coordinate for the square: "))
    new_square(square_x, square_y)

    # Getting coordinates from user for the new circle
    circle_x = float(input("enter the x coordinate for the circle: "))
    circle_y = float(input("enter the y coordinate for the circle: "))
    new_circle(circle_x, circle_y)

    #keeping turtle page open until user manually closing it
    turtle.mainloop()

if __name__ == "__main__":
    main()
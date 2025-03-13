#Preston
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle for drawing
artist = turtle.Turtle()
artist.shape("turtle")
artist.speed(10)

# Function to draw a simple figure (Human-like form for characters)
def draw_figure(x, y, color, size=50):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.color(color)
    artist.begin_fill()
    artist.circle(size)  # Head
    artist.end_fill()

    # Body
    artist.goto(x, y - size)
    artist.setheading(270)
    artist.pendown()
    artist.forward(2 * size)

    # Arms
    artist.penup()
    artist.goto(x - size, y - size / 2)
    artist.setheading(180)
    artist.pendown()
    artist.forward(1.5 * size)

    artist.penup()
    artist.goto(x + size, y - size / 2)
    artist.setheading(0)
    artist.pendown()
    artist.forward(1.5 * size)

# Function to draw sword
def draw_sword(x, y):
    artist.penup()
    artist.goto(x, y)
    artist.setheading(90)
    artist.pendown()
    artist.pensize(5)
    artist.color("gray")
    artist.forward(100)
    artist.penup()
    artist.pensize(1)

# Function to draw wings (simplified)
def draw_wings(x, y, direction="left"):
    artist.penup()
    artist.goto(x, y)
    artist.setheading(45 if direction == "left" else 135)
    artist.pendown()
    artist.color("white")
    artist.begin_fill()
    artist.circle(60, 180)  # Half-circle for a wing
    artist.end_fill()

# Draw Sanguinius (with wings and sword)
draw_wings(-100, 100, "left")
draw_wings(100, 100, "right")
draw_figure(0, 50, "yellow")
draw_sword(0, 50)

# Draw Horus (without wings, holding a sword)
draw_figure(150, -100, "red")  # Horus as a red figure
draw_sword(150, -50)

# Hide the turtle
artist.hideturtle()

# Keep the window open
turtle.done()

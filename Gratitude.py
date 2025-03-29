import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Thank You ISRO!")
screen.bgcolor("black")  # Space-like background

# Create a turtle object for drawing
pen = turtle.Turtle()
pen.speed(3)
pen.color("white")
pen.hideturtle()

# Function to write text
def write_message(message, font_size, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(message, align="center", font=("Arial", font_size, "bold"))

# Draw the gratitude message
write_message("Thank You ISRO!", 24, 0, 100)
write_message("For Inspiring the World with Your Space Missions!", 16, 0, 50)

# Create a turtle for the rocket
rocket = turtle.Turtle()
rocket.speed(3)
rocket.color("orange")
rocket.shape("triangle")
rocket.shapesize(2, 1)
rocket.penup()
rocket.goto(0, -100)

# Draw a simple Earth at the bottom
earth = turtle.Turtle()
earth.speed(0)
earth.color("blue")
earth.penup()
earth.goto(0, -200)
earth.pendown()
earth.begin_fill()
earth.circle(50)
earth.end_fill()
earth.hideturtle()

# Add some green patches on Earth
for _ in range(3):
    earth.penup()
    earth.goto(0 + _ * 10, -200 + _ * 5)
    earth.pendown()
    earth.color("green")
    earth.begin_fill()
    earth.circle(10)
    earth.end_fill()

# Animate the rocket moving upwards
for i in range(50):
    rocket.goto(0, -100 + i * 5)
    time.sleep(0.05)

# Add a final message
write_message("Proud of Your Achievements!", 14, 0, -50)

# Keep the window open until clicked
screen.exitonclick()
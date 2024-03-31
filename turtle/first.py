import turtle

# Create a turtle object
t = turtle.Turtle()

# Function to draw a square
def draw_square():
    for _ in range(4):
        t.forward(100)  # Move the turtle forward by 100 units
        t.right(90)     # Turn the turtle right by 90 degrees

# Main function
def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    screen.title("Turtle Square Example")

    # Call the draw_square function
    draw_square()

    # Keep the window open until it is closed by the user
    turtle.done()

# Call the main function
if __name__ == "__main__":
    main()

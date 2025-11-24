import turtle

# --- Configuration ---
# Set up constants for an easy-to-manage grid size
CELL_SIZE = 40  # Length of one side of a single grid cell
MAZE_WIDTH = 5  # The number of cells wide/high
START_X = -100  # Top-left start X coordinate
START_Y = 100   # Top-left start Y coordinate
TOTAL_LENGTH = MAZE_WIDTH * CELL_SIZE # 5 * 40 = 200

game_running = True

# --- Turtle Setup ---
turtle.setup(500, 500)
wn = turtle.Screen()
wn.title("Grid Maze Recreation")
wn.bgcolor("lightgreen") # Keeping your original background color

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.penup()
# Tess starts inside the first cell (centered)
tess.goto(START_X + (CELL_SIZE / 2), START_Y - (CELL_SIZE / 2)) 

# --- Timer Display Turtle ---
timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
timer_pen.goto(0, 150) # Position the timer at the top center
timer_pen.color("red")
timer_pen.write("Time Left: 5.0s", align="center", font=("Arial", 18, "bold"))

maze_maker = turtle.Turtle()
maze_maker.color("black")
maze_maker.pensize(5) # Using a moderate line thickness
maze_maker.speed(0)  # Fastest drawing speed
maze_maker.hideturtle()

# Helper function to draw a wall segment
def draw_wall(x1, y1, x2, y2):
    """Moves the maze_maker to (x1, y1) and draws a line to (x2, y2)."""
    maze_maker.penup()
    maze_maker.goto(x1, y1)
    maze_maker.pendown()
    maze_maker.goto(x2, y2)

# --- 🚧 Build the Maze (Replaces your loop) ---
# The logic here is to draw the outer border and then draw specific internal walls
# to define the paths, mimicking the structure in your image.

## 1. Draw the Outer Border
end_x = START_X + TOTAL_LENGTH
end_y = START_Y - TOTAL_LENGTH

# Top Wall (with entrance gap)
draw_wall(START_X + CELL_SIZE, START_Y, end_x, START_Y) # Gap for entrance at (START_X, START_Y)

# Right Wall
draw_wall(end_x, START_Y, end_x, end_y)

# Bottom Wall (with exit gap)
draw_wall(end_x - CELL_SIZE, end_y, START_X, end_y) # Gap for exit at (end_x, end_y)

# Left Wall
draw_wall(START_X, end_y, START_X, START_Y)


## 2. Draw Internal Walls
# Coordinates are defined relative to the START_X and START_Y corner.
# Wall Format: (x1, y1, x2, y2)

internal_walls = [
    # Horizontal Walls (across the columns)
    (START_X + CELL_SIZE, START_Y - CELL_SIZE, START_X + CELL_SIZE * 3, START_Y - CELL_SIZE),
    (START_X, START_Y - CELL_SIZE * 2, START_X + CELL_SIZE, START_Y - CELL_SIZE * 2),
    (START_X + CELL_SIZE * 2, START_Y - CELL_SIZE * 2, START_X + CELL_SIZE * 4, START_Y - CELL_SIZE * 2),
    (START_X + CELL_SIZE, START_Y - CELL_SIZE * 3, START_X + CELL_SIZE * 2, START_Y - CELL_SIZE * 3),
    (START_X + CELL_SIZE * 3, START_Y - CELL_SIZE * 3, START_X + CELL_SIZE * 5, START_Y - CELL_SIZE * 3),
    (START_X + CELL_SIZE * 2, START_Y - CELL_SIZE * 4, START_X + CELL_SIZE * 3, START_Y - CELL_SIZE * 4),
    (START_X + CELL_SIZE * 4, START_Y - CELL_SIZE * 4, START_X + CELL_SIZE * 5, START_Y - CELL_SIZE * 4),

    # Vertical Walls (down the rows)
    (START_X + CELL_SIZE, START_Y - CELL_SIZE * 3, START_X + CELL_SIZE, START_Y - CELL_SIZE * 5),
    (START_X + CELL_SIZE * 2, START_Y - CELL_SIZE, START_X + CELL_SIZE * 2, START_Y - CELL_SIZE * 2),
    (START_X + CELL_SIZE * 3, START_Y - CELL_SIZE * 2, START_X + CELL_SIZE * 3, START_Y - CELL_SIZE * 4),
    (START_X + CELL_SIZE * 4, START_Y - CELL_SIZE, START_X + CELL_SIZE * 4, START_Y - CELL_SIZE * 2),
    (START_X + CELL_SIZE * 4, START_Y - CELL_SIZE * 3, START_X + CELL_SIZE * 4, START_Y - CELL_SIZE * 4),
    
]

# Draw all the internal walls
for wall in internal_walls:
    draw_wall(wall[0], wall[1], wall[2], wall[3])

def countdown(seconds_left):
    """Recursively updates the timer display."""
    global game_running

    if seconds_left >= 0:
        # Update the display
        timer_pen.clear()
        timer_pen.write(f"Time Left: {seconds_left:.1f}s", align="center", font=("Arial", 18, "bold"))

        # Schedule the next update 100 milliseconds (0.1 seconds) later
        wn.ontimer(lambda: countdown(seconds_left - 0.1), 100)
    else:
        # Time has run out! Stop the game and show the message.
        game_running = False
        timer_pen.goto(0, 0)
        timer_pen.color("black")
        timer_pen.write("❌ TIME'S UP! ❌", align="center", font=("Arial", 30, "bold"))
        tess.color("gray") # Change player color to indicate loss


def h1():
    tess.forward(10)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

countdown(5.0)

# Tell the window to start listening for events.
wn.listen()
wn.mainloop()
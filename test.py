import turtle as trtl
import random


APPLE_IMAGE = "apple.gif"          
BACKGROUND_IMAGE = "background.gif"
font_setup = ("Arial", 30, "bold")
letter_list = list("abcdefghijklmnopqrstuvwxyz")
current_letter = ""           

apple = trtl.Turtle() 
accuracy_score = 0 
incorrect_score = 0 
timer_seconds = 30 

# Timer variables
timer = 30
counter_interval = 1000 
timer_up = False 
score = 0 

counter = trtl.Turtle() 

# set up the screen
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic(BACKGROUND_IMAGE)
wn.addshape(APPLE_IMAGE)

score_writer = trtl.Turtle()

score_writer.penup() 
score_writer.hideturtle()
score_writer.goto(-200, 250) 


apple.penup()
apple.hideturtle()


counter.penup()
counter.hideturtle()
counter.goto(200, 250) 


for letter in "abcdefghijklmnopqrstuvwxyz":
    wn.onkeypress(None, letter)





def generate_random_letter():
    """
    Choose a random letter from letter_list and remove it.
    Return the letter.
    If letter_list is empty, return "".
    """
    global current_letter, letter_list
    if len(letter_list)==0:
        current_letter = ""
        return ""
    else:
        number_of_letters = len(letter_list)
        slot = random.randint(0,number_of_letters-1)
        current_letter=letter_list.pop(slot)
        return current_letter 


def get_random_xy():
    x = random.randint(-300,300)
    y = random.randint(50, 250)
    return (x,y)

def draw_apple_and_letter():
    global current_letter
    if not timer_up:
        apple.clear()         
        apple.shape(APPLE_IMAGE)
        apple.showturtle()


    current_letter = generate_random_letter()
    if current_letter=="":
        return
    location = get_random_xy() 
    apple.hideturtle()
    apple.goto(location[0], location[1])
    apple.showturtle()
    apple.write(current_letter, align="center", font=("Arial", 74, "bold"))
    return


def drop_apple():
    """
    Make the apple fall straight down and then draw a new apple and letter.
    """
    global apple
    xcoord = apple.xcor()
    ycoord = apple.ycor()
    apple.goto(xcoord, ycoord-250)
    apple.clear()
    apple.hideturtle()
    draw_apple_and_letter()

def update_score_display():
    """
    Clears the old score and writes the current accuracy and incorrect scores.
    """
    global score_writer, accuracy_score, incorrect_score, font_setup
    score_writer.clear()
    score_text = f"Correct: {accuracy_score}\nIncorrect: {incorrect_score}"
    score_writer.write(score_text, align="center", font=("Arial", 20, "normal")) 


# ------------- key handling -------------

def handle_key(letter_pressed):

    """
    Called when a key is pressed.
    If the key matches the current letter, drop the apple.
    """
    global current_letter
    global accuracy_score
    global incorrect_score

    if timer_up:
        return

    # Check if the pressed key matches the letter on the apple
    if letter_pressed == current_letter:
        print("Correct key! (Pressed: " + letter_pressed + ")")
        drop_apple()
        accuracy_score += 1

    else:
        print(f"Incorrect key. Pressed: {letter_pressed}, Needed: {current_letter}")
        incorrect_score += 1
    
    update_score_display() #
  

def countdown():
    global timer, timer_up, counter
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", align="center", font=font_setup)
        timer_up = True
      
        apple.clear()
        apple.hideturtle()
    else:
        
        counter.write("Timer: " + str(timer), align="center", font=font_setup)
        timer -= 1
       
        counter.getscreen().ontimer(countdown, counter_interval)


# individual key functions 
def press_a():
    handle_key("a")
def press_b():
    handle_key("b")
def press_c():
    handle_key("c")
def press_d():
    handle_key("d")
def press_e():
    handle_key("e")
def press_f():
    handle_key("f")
def press_g():
    handle_key("g")
def press_h():
    handle_key("h")
def press_i():
    handle_key("i")
def press_j():
    handle_key("j")
def press_k():
    handle_key("k")
def press_l():
    handle_key("l")
def press_m():
    handle_key("m")
def press_n():
    handle_key("n")
def press_o():
    handle_key("o")
def press_p():
    handle_key("p")
def press_q():
    handle_key("q")
def press_r():
    handle_key("r")
def press_s():
    handle_key("s")
def press_t():
    handle_key("t")
def press_u():
    handle_key("u")
def press_v():
    handle_key("v")
def press_w():
    handle_key("w")
def press_x():
    handle_key("x")
def press_y():
    handle_key("y")
def press_z():
    handle_key("z")



# ------------- basic setup and start -------------

# draw the first apple and letter
draw_apple_and_letter()
print(get_random_xy())


countdown()

# connect keys
wn.onkeypress(press_a, "a")
wn.onkeypress(press_b, "b")
wn.onkeypress(press_c, "c")
wn.onkeypress(press_d, "d")
wn.onkeypress(press_e, "e")
wn.onkeypress(press_f, "f")
wn.onkeypress(press_g, "g")
wn.onkeypress(press_h, "h")
wn.onkeypress(press_i, "i")
wn.onkeypress(press_j, "j")
wn.onkeypress(press_k, "k")
wn.onkeypress(press_l, "l")
wn.onkeypress(press_m, "m")
wn.onkeypress(press_n, "n")
wn.onkeypress(press_o, "o")
wn.onkeypress(press_p, "p")
wn.onkeypress(press_q, "q")
wn.onkeypress(press_r, "r")
wn.onkeypress(press_s, "s")
wn.onkeypress(press_t, "t")
wn.onkeypress(press_u, "u")
wn.onkeypress(press_v, "v")
wn.onkeypress(press_w, "w")
wn.onkeypress(press_x, "x")
wn.onkeypress(press_y, "y")
wn.onkeypress(press_z, "z")


wn.listen()
wn.update()
trtl.mainloop()

print(f"Final Accuracy Score: {accuracy_score}")
print(f"Final Incorrect Score: {incorrect_score}")
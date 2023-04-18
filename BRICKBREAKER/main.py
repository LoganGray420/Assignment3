#Importing the pygame zero library so we can use its functions
import pgzrun

#Naming our game/window
TITLE = "Brickbreaker"

#Setting the width of the window to 640 pixels
WIDTH = 640
#Setting the height of the window to 480 pixels
HEIGHT = 480
#Setting a variable that sets 10 bricks in a row
BRICKS_PER_ROW = 10

#Declaring our paddle as an actor so we can use it and adding an image to it ensuring the image is in all lowercase
paddle = Actor("paddleblu.png")
#Setting the paddle starting x coordinate
paddle.x = 320
#Setting the paddle starting y coordinate
paddle.y = 440
#Declaring our ball as an actor so we can use it and adding an image to it ensuring the image is in all lowercase
ball = Actor("ballgrey.png")
#Ball starting x coordinates
ball.x = 320
#Ball starting y coordinates
ball.y = 340
#Ball starting speed in the x direction 3 units per tick
ball_x_speed = 3
#Ball starting speed in the y direction 3 units per tick
ball_y_speed = 3
#Setting time as a global variable so we can easily call it
global time
#Setting times base value to 0 so the timer starts at 0
time = 0
#Time x coordinate is 0
timer_x = 0
#Timer y coordinate is the entire height minus 20 pixels so it sits in the bottom left corner
timer_y = HEIGHT - 20
#Setting the default condition to false so it needs to be triggered
win = False
#Setting the default condition to false so it needs to be triggered
game_over = False
#Setting score as a global variable so we can easily call it
global score
#Setting our base score to 0 and assigning a value to it
score=0
#Setting a variable for the score incrimenting by one 
score_increment=1
skill_issue=False
congrats_sailor=False

#Creating an empty array to store the bricks once they've been clear
bricks = []
#Creating a starting point for the bricks and setting how each brick is spaced out in the x direction
initial_brick_pos_x = 64 / 2
#Creating a starting point for the bricks and setting how each brick is spaced out in the y direction
initial_brick_pos_y = 32 / 2
#brick sprites are 64x32
#Adding sprites to the bricks from our attached folder
brick_sprites = ["element_grey_rectangle.png", "element_red_rectangle.png", "element_blue_rectangle.png"]

#Creating our function that handles all images being place in the game
def draw():
    #Creating the colour of our background (RGB scale)
    screen.fill((181, 126, 220 ))
    #If the "win" condition is met ie clearing all the bricks
    if win:
        #Displaying a message that you won and stating the location of it
        screen.draw.text("YOU WIN!", (WIDTH // 2 - 40, HEIGHT // 2))
        #Displaying the final score, acessing the score as a string, using x,y coordinates to place it, font colour(white) and font size
        screen.draw.text('Final Score: ' + str(score), (190, 350), color=(255,255,255), fontsize=60)
        #Displaying the restart message with the location
        screen.draw.text('Press R to play again',(WIDTH // 2 - 60, HEIGHT // 4))
        #Creating a global variable for the game_over variable
        global game_over
        #Needed to use this again in the function
        game_over=False
        global timer_x
        #Hiding the timer off screen since it was easier than freezing it
        timer_x= 999999
        global congrats_sailor
        #Creating an if statement so the sound effect only plays once and doesn't loop
        if congrats_sailor==False:
            #Makes it so the trigger is met for Congrats Sailor to play
            congrats_sailor=True
            #Plays the sound effect for "congrats sailor"
            sounds.congrats_sailor.play()
        #If statement letting the user press r to restart the game
        if keyboard.r:
             #Runs our default function that sets the game back to the start
             default()
        return
    #If loop that triggers if the ball is below the paddle
    if game_over:
        #Game over message
        screen.draw.text("GAME OVER", (WIDTH // 2 - 60, HEIGHT // 2))
        screen.draw.text('Final Score: ' + str(score), (190, 350), color=(255,255,255), fontsize=60)
        screen.draw.text('Press R to play again',(WIDTH // 2 - 60, HEIGHT // 4))
        game_over=False
        timer_x= 999999
        #Creating a global variable for "Skill Issue"
        global skill_issue
        #Creating a condition that once in the game over state if skill_issue is false it will trigger but it only loops once
        if skill_issue == False:
            skill_issue=True
            #Plays the "Skill Issue" sound effect
            sounds.skill_issue.play()
        if keyboard.r:
             default()
    #Displaying our timer at its assigned coordinates and accessing it as a string
    screen.draw.text(str(time), (timer_x, timer_y))

    #Displaying the paddle on screen
    paddle.draw()
    #Displaying the ball on screen
    ball.draw()

    #Creating a for loop for every individual brick in our bricks array
    for brick in bricks:
        #Displaying each individual brick
        brick.draw()
    #Displaying our score in the bottom right
    screen.draw.text('Score: ' + str(score), (550,460), color=(255,255,255), fontsize=30)

#Function that operates our paddle and makes it easier to update the game constantly calling this function
def update_paddle():
    #If the left arrow key is pressed:
    if keyboard.left:
        #Setting a boundry for our paddle so it cannot go off screen on the left side. +48 accounts for the 48 pixels on the left side
        #of the paddle since it's boundry is based around the middle point
        if(paddle.x - 4 > 0 + 48):
            paddle.x = paddle.x - 4
    #If the right arrow key is pressed:
    if keyboard.right:
        #Setting the right side boundry for the paddle
        if(paddle.x  + 4 < 640 - 48):
            paddle.x = paddle.x + 4  

#Creating a function that updates the score
def update_score():
    #Creating a global variable for the score so it works properly in the function
    global score
    #Increasing the score by 1 every time the condition is met
    score= score+ score_increment 
        
#Function that handles mouse movements at the position of the cursor
def on_mouse_move(pos):
    #Connecting the paddle in the x direction with the cursor
    paddle.x = pos[0]
    
    if paddle.x < (paddle.width / 2):
        paddle.x = paddle.width / 2
    if paddle.x >= (WIDTH - 48):
        paddle.x = (WIDTH - 48 - 1)

#Function to update the balls logic
def update_ball():
    #Global variables for the balls speed in the x and y directions
    global ball_x_speed
    global ball_y_speed
    #Subtracting the balls speed from the location so it shifts 
    ball.x = ball.x - ball_x_speed
    ball.y = ball.y - ball_y_speed

    #Declaring the game over variable in this function
    global game_over
    #If statement for if the ball is below the paddle
    if not game_over and ball.y > paddle.y:
        #Trigger a game over
        game_over = True
        return
    #If the ball hits either edge it will bounce 
    if(ball.x > WIDTH) or (ball.x < 0):
        ball_x_speed = ball_x_speed * -1

    #If the ball hits the ceiling or floor it will bounce 
    if(ball.y > HEIGHT) or (ball.y < 0):
        ball_y_speed = ball_y_speed * -1

    #If the ball makes contact with the paddle
    if ball.colliderect(paddle):
        #Bounce and change the speed in the y direction
        ball_y_speed = ball_y_speed * -1
        #Play the "okay" sound effect 1 time when the ball contacts the paddle
        sounds.okay.play()

    #For loop that triggers for every individual brick in the entire bricks array
    for brick in bricks:
        #If statment on if the ball makes contact with a brick
        if ball.colliderect(brick):
            #Delete the brick
            bricks.remove(brick)
            #Increase the score
            update_score()
            #Trigger the "woah" sound effect
            sounds.woah.play()
            #Change the direction of the ball
            ball_y_speed = ball_y_speed * -1
    #Setting our global variable for the win condition
    global win
    #Triggering our win condition if the amount of bricks is =0
    win = len(bricks) == 0

#Function that updates all of our components of the game every time it ticks
def update(dt):
    global time
    global score
    global game_over
    #Adding a time incriment to our timer
    time += dt
    #Rounds our timer off at 2 decimal places
    time=round(time,2)
    update_paddle()
    update_ball()

#Function that places the bricks in the row without overlapping
def place_brick_row(sprite, pos_x, pos_y):
    #Every time the brick is in range set by the variable of BRICKS_PER_ROW
    for i in range(BRICKS_PER_ROW):
        #Declaring the brick as an actor using the sprites from the start
        brick = Actor(sprite)
        #Places a brick in the x direction every 64 pixels so they don't overlap
        brick.x = pos_x + i * 64
        #Places a brick in the y direction 
        brick.y = pos_y
        #Adds the brick to the list of bricks so it can be deleted if contacted
        bricks.append(brick) 
#Function that we call to reset the game when the player either wins or losses and presses r. It sets every position and value back to
#its original amount/spot. It resets condition for certain sound effects too so they don't loop. 
def default():
    global time
    time=0
    global timer_x
    timer_x=0
    global score
    score=0
    global bricks
    bricks=[]
    global initial_brick_pos_y
    #Using this but not the x since we modify the y coordinates and needed the bricks to not be lower everytime the player restarts
    #This acts as a bottom for the bricks so they can't get too low
    initial_brick_pos_y = 32/2
    for brick_sprite in brick_sprites:
        place_brick_row(brick_sprite, initial_brick_pos_x, initial_brick_pos_y)
        initial_brick_pos_y +=32 
    ball.x=320
    ball.y=340
    paddle.x=320
    paddle.y=440
    global skill_issue
    skill_issue=False
    global congrats_sailor
    congrats_sailor=False

#For loop that palces each individual brick in our overall variable
for brick_sprite in brick_sprites:
    #Taking the brick sprite and placing them in their initial positions
    place_brick_row(brick_sprite, initial_brick_pos_x, initial_brick_pos_y)
    #Places the next brick in the column 32 pixels below the last
    initial_brick_pos_y += 32

#Runs the program
pgzrun.go() 
from tkinter import *
import random
import os
import sys
GAME_WIDTH = 600
GAME_HEIGHT =600
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
color = ['green', 'yellow','red']
color2 = ['#27FF1C', '#FFFB1C', '#FF1C1C']
tint = 0
SNAKE_COLOR = color2[0]
FOOD_COLOR = random.choice(color)
BACKGROUD_COLOR = 'black'
score = 0
class snake():
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)

class Food():
    def __init__(self):
        global FOOD_COLOR
        global color
        global score
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]
        if FOOD_COLOR == color[0]:
            FOOD_COLOR = color[1]
        elif FOOD_COLOR == color[1]:
            FOOD_COLOR = color[2]
        else:
            FOOD_COLOR = color[0]
        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
        if score > 5:
            canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
def next_turn(snake, food):
    global score
    global SNAKE_COLOR
    global color2
    global tint
    x,y = snake.coordinates[0]
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x,y))
    if score >= 3:
        if tint == (len(color2) -1):
            tint = 0
        else:
            tint += 1
        if score >= 6:
            if tint == (len(color2) -1):
                tint = 0
            else:
                tint += 1
            if score >=9:
                if tint == (len(color2) -1):
                    tint = 0
                else:
                    tint += 1
    SNAKE_COLOR = color2[tint]
    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text='Score: {}'.format(score))
        canvas.delete("food")
        food = Food()
    else:

        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)
    
def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x,y = snake.coordinates[0]
    if x< 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x== body_part[0] and y == body_part[1]:
            return True

def new_game():
    python = sys.executable
    os.execl(python,python, * sys.argv) 
    

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70, ), text='GAME OVER', fill='red',tag='gameover')
window = Tk()
window.title('Snake game')
window.resizable(False, False)

direction = 'down'
label = Label(window, text='score:{}'.format(score), font=('consolas',40))
label.pack(side='bottom')
button = Button(text= "restart", font=("consolas",20), command =new_game)
button.pack(side='top')
canvas = Canvas(window, bg=BACKGROUD_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()


window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (screen_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
      
snake =  snake()
food = Food()
next_turn(snake, food)
window.mainloop()
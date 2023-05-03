from tkinter import *
import random
games = 0
x_wins = 0
o_wins = 0
def next_turn(row, column):
    global games
    global player
    global x_wins
    global o_wins
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
                games += 1
                x_wins += 1
                score.config(text= "Game:" + str(games) + "   (X wins):" + str(x_wins) + "   (O wins):" + str(o_wins))
            
            elif check_winner() == "Tie!":
                label.config(text=("Tie!"))
                games += 1
                score.config(text= "Game:" + str(games) + "   (X wins):" + str(x_wins) + "   (O wins):" + str(o_wins))
            
        else:
            player = players[1]
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))
                games += 1
                o_wins += 1
                score.config(text= "Game:" + str(games) + "   (X wins):" + str(x_wins) + "   (O wins):" + str(o_wins))
            
            elif check_winner() == "Tie!":
                label.config(text=("Tie!"))
                games += 1
                score.config(text= "Game:" + str(games) + "   (X wins):" + str(x_wins) + "   (O wins):" + str(o_wins))

def check_winner():
    global games
    for row in range(3):
        if buttons [row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg="blue")
            buttons[row][1].config(bg="blue")
            buttons[row][2].config(bg="blue")
            return True

    for column in range(3):
        if buttons [0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg="blue")
            buttons[1][column].config(bg="blue")
            buttons[2][column].config(bg="blue")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][2].config(bg="blue")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][0].config(bg="blue")
        return True

    elif empty_space() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="gold")
        return "Tie!"

    else:
        return False

def empty_space():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1
    if spaces == 0:
        return False

    else:
        return True

def new_game():

    global player
    player = random.choice(players)
    label.config(text= player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", fg= 'green', bg= 'black')

window = Tk()
window.title("Tic-Tac-Toe")
players = ['X','O']
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
score = Label(text= "Game:" + str(games) + " X wins:" + str(x_wins) + " O wins:" + str(o_wins), font=('consolas',20))
score.pack(side='bottom')
label = Label(text= player + " turn", font=('consolas',40))
label.pack(side="top")
reset_btn = Button(text= "restart", font=("consolas",20), command =new_game)
reset_btn.pack(side="top")
frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=("consolas",40), width=5, height=2, command= lambda row = row, column = column: next_turn(row, column), fg= 'green', bg= 'black')
        buttons[row][column].grid(row = row, column= column)

window.mainloop()
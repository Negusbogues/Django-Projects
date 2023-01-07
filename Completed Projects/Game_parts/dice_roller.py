from tkinter import *
import random
window = Tk()
window.geometry("400x400")
window.title('Dice Roller')
window.config(background='black')
label = Label(window, text= '', font= ('times', 100), foreground= "green", background= 'black')
text_label = Label(window, text='', font= ('times', 30), foreground= "green", background= 'black')

def dice_roll():
    doubles = False
    dice = [1,2,3,4,5,6]
    roll = random.choice(dice),random.choice(dice)
    total = sum(roll)
    if roll[0] == roll[1] and roll[0] != 1:
        if total == 8:
            doubles = True
            print(f"Doubles! \n{total}, {roll}")
            text_label.config(text= '', font= ('times', 30), foreground= "green", background= 'black')
            text_label.config(text= f"Doubles!\nYou rolled an {total}", font= "helvetica 30 bold", fg='white')
            text_label.pack(side='bottom')
            label.config(text= f"{roll}")
            label.pack()    
        else:
            doubles = True
            print(f"Doubles! \n{total}, {roll}")
            text_label.config(text= '', font= ('times', 30), foreground= "green", background= 'black')
            text_label.config(text= f"Doubles!\nYou rolled a {total}", font= "helvetica 30 bold", fg='white')
            text_label.pack(side='bottom')
            label.config(text= f"{roll}")
            label.pack()    
    elif roll[0] == roll[1]:
        doubles = True
        if roll[0] == 1:
            print(f'Snake Eyes! \n{total}, {roll}')
            text_label.config(text= '', font= ('times', 30), foreground= "green", background= 'black')
            text_label.config(text= "Snake Eyes!\nYou rolled a 2", font= "helvetica 30 bold", fg='yellow')
            text_label.pack(side='bottom')
            label.config(text= f"{roll}")
            label.pack()
    elif total == 11 or total == 8:
        print(f"You rolled an {total}, {roll}")
        text_label.config(text= '', font= ('times', 30), foreground= "green", background= 'black')
        text_label.config(text= f"You rolled an {total}!")
        text_label.pack(side='bottom')
        label.config(text= f"{roll}")
        label.pack()
    else:
        print(f"You rolled a {total}, {roll}")
        text_label.config(text= '', font= ('times', 30), foreground= "green", background= 'black')
        text_label.config(text= f"You rolled a {total}!")
        text_label.pack(side='bottom')
        label.config(text= f"{roll}")
        label.pack()

roll_button = Button(text= "ROLL", font= ('consolas', 22), fg= 'green', bg= "black", width= 6, height= 2, command= dice_roll, border= 5)
roll_button.pack(side= 'top')
frame = Frame(window)
frame.pack()

window.mainloop()
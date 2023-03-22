from tkinter import *
import random

colours = ['Red','Blue','Green','Pink','Yellow','Orange','White','Purple','Brown','Grey']
score = 0
timeleft = 45

def start(event):  
    if timeleft == 45:
        time()
    next()

def next():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0,END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score))

def time():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: "+ str(timeleft))
        timeLabel.after(1000, time)
    elif timeleft==0:
        Label1=Label(text="Thank you for playing the game \n Your score is "+str(score),font=(20)).pack()
        button=Button(text="Back to Menu").pack()

roothg1=Tk()
roothg1.title("COLORGAME")

instructions =Label(roothg1, text = "Type in the colour of the words, and not the word text!",font=16)
instructions.pack()

scoreLabel=Label(roothg1, text = "Press enter to start",font=16)
scoreLabel.pack()

timeLabel=Label(roothg1, text = "Time left: " + str(timeleft))
timeLabel.pack()

label=Label(roothg1,font=('Algerian',60),background="black")
label.pack()

e=Entry(roothg1)
roothg1.bind('<Return>', start)
e.pack()
e.focus_set()


roothg1.mainloop()



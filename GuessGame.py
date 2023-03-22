import tkinter;
from PIL import Image, ImageTk;
import random;

rootzg2 = tkinter.Tk()
rootzg2.title('Guess the number!')
#rootzg2eval('tk::PlaceWindow . center')
#rootzg2iconbitmap()
rootzg2.geometry('600x400')
rootzg2.resizable(width=False,height=False)
imB = Image.open(r'bgzg2.jpg')
phB = ImageTk.PhotoImage(imB)

labelBG = tkinter.Label(rootzg2, image=phB)
labelBG.place(x=0, y=0)

TARGET = random.randint(0, 20)
RETRIES = 20
 

def update_result(text):
    result.configure(text=text)

def new_game():
    global TARGET, RETRIES
    TARGET = random.randint(0, 20)
    RETRIES = 20
    update_result(text="Guess a number between\n 1 and 20")

def play_game():
    global RETRIES
 
    choice = int(number_form.get())
     
    if choice != TARGET:
        RETRIES -= 1
     
        result = "Wrong Guess!! Try Again"
        if TARGET < choice:
            hint = "The required number lies between 0 and {}".format(choice)
        else:
            hint = "The required number lies between {} and 20".format(choice)
        result = result + "\n\nHINT :\n" + hint
     
    else:
        result = "Your score is {}".format(RETRIES)
        result += "\n" + "Start a new game"
     
    update_result(result)

title = tkinter.Label(rootzg2,text="Guess The Number",font=("Arial",24),fg="#fffcbd",bg="#065569")

result = tkinter.Label(rootzg2, text="Guess a Number between 1 and 20!", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tkinter.LEFT)

imN = Image.open(r'newzg2.png')
phN = ImageTk.PhotoImage(imN)
play_button = tkinter.Button(rootzg2, image=phN, font=("Arial", 14, "bold"), fg = "Black", bg="black", command=new_game)

imG = Image.open(r'checkzg2.png')
phG = ImageTk.PhotoImage(imG)
guess_button = tkinter.Button(rootzg2,image=phG,font=("Arial",13), fg="#13d675",bg="Black", command=play_game)


guessed_number = tkinter.StringVar()
number_form = tkinter.Entry(rootzg2,font=("Arial",11),textvariable=guessed_number)

title.place(x=170, y=50)
result.place(x=180, y=210)

guess_button.place(x=350, y=147) 
play_button.place(x=250, y=320)

number_form.place(x=180, y=160)

rootzg2.mainloop()
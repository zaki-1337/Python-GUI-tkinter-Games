import tkinter;
from PIL import Image, ImageTk;
import random;

rootzg1 = tkinter.Tk()
rootzg1.title('Pig Game')
#rootzg1.eval('tk::PlaceWindow . center')
#rootzg1.iconbitmap()
rootzg1.geometry('500x450')
rootzg1.resizable(width=False,height=False)

imB = Image.open(r'bgzg1.jpg')
phB = ImageTk.PhotoImage(imB)

labelBG = tkinter.Label(rootzg1, image=phB)
labelBG.place(x=0, y=0)

dice = [r'die1.png',
        r'die2.png',
        r'die3.png',
        r'die4.png',
        r'die5.png',
        r'die6.png']

im = Image.open(r'die0.png')
ph = ImageTk.PhotoImage(im)
labelImage = tkinter.Label(rootzg1, image=ph)
labelImage.pack( side = tkinter.BOTTOM ,padx=10,pady=10)

player1=1
player2=0
score1=0
score2=0
currentHold=0
playerS=('1','2')
playerC=('#76EE00','red')


def new_game():
    labelImage.configure(image=ph)
    global currentHold, player1, player2, score1, score2, playerS, playerC
    player1=1
    player2=0
    currentHold=0
    score1=0
    score2=0
    playerS=('1','2')
    labelP1S.configure(text=score1)
    labelP2S.configure(text=score2)
    labelRoll.configure(text=currentHold)
    

labelP1 = tkinter.Label(rootzg1, text='Player 1', bg=playerC[0])
labelP1.pack( side = tkinter.LEFT,padx=10,pady=10 )
labelP1S = tkinter.Label(rootzg1, text='0')
labelP1S.pack( side = tkinter.LEFT,padx=10,pady=10)

labelP2 = tkinter.Label(rootzg1, text='Player 2', bg=playerC[1])
labelP2.pack( side = tkinter.RIGHT,padx=10,pady=10)
labelP2S = tkinter.Label(rootzg1, text='0')
labelP2S.pack( side = tkinter.RIGHT,padx=10,pady=10)

labelRoll = tkinter.Label(rootzg1, text='0')
labelRoll.pack(side = tkinter.BOTTOM,padx=10,pady=10)

def roll_dice():
    roll1 = random.choice([0,1,2,3,4,5])
    image1 = ImageTk.PhotoImage(Image.open(dice[roll1]))
    labelImage.configure(image=image1)
    labelImage.image = image1
    global currentHold, player1, player2, score1, score2, playerS, playerC
    if (roll1!=0):
        currentHold=currentHold+roll1+1;
        labelRoll.configure(text=currentHold)
    elif(roll1==0):
        currentHold=0
        labelRoll.configure(text=currentHold)
        player1= 1 - player1
        player2 = 1 - player2
        playerC=tuple(reversed(playerC))
        labelP1.configure(bg=playerC[0])
        labelP2.configure(bg=playerC[1])
        playerS=tuple(reversed(playerS))
        
imC = Image.open(r'confzg1.jpg')
phC = ImageTk.PhotoImage(imC)

def open_popup():
    topR= tkinter.Toplevel(rootzg1)
    topR.geometry("200x50")
    topR.title("Result")
    topR.transient(rootzg1)
    topR.lift(rootzg1)
    rootzg1_x = rootzg1.winfo_rootzg1x()
    rootzg1_y = rootzg1.winfo_rootzg1y()
    win_x = rootzg1_x + 300
    win_y = rootzg1_y + 100
    topR.geometry(f'+{win_x}+{win_y}')
    tkinter.Label(topR, text= "Player {0[0]} Wins!".format(playerS), font=('Mistral 18 bold'), fg='white', compound='center',
                  image=phC).pack(side=tkinter.TOP)
        
def hold_lol():
    global currentHold, player1, player2, score1, score2, playerS, playerC
    if (player1):
        score1+=currentHold
        labelP1S.configure(text=score1)
        if (score1>=100):
            open_popup()
            new_game()
            return
        player1= 1 - player1
        player2 = 1 - player2
        playerC=tuple(reversed(playerC))
        labelP1.configure(bg=playerC[0])
        labelP2.configure(bg=playerC[1])
        playerS=tuple(reversed(playerS))
        currentHold=0
        labelImage.configure(image=ph)
        labelRoll.configure(text='0')
    elif(player2):
        score2+=currentHold
        labelP2S.configure(text=score2)
        if (score2>=100):
            open_popup()
            new_game()
            return
        player1 = 1 - player1
        player2 = 1 - player2
        playerC=tuple(reversed(playerC))
        labelP1.configure(bg=playerC[0])
        labelP2.configure(bg=playerC[1])
        playerS=tuple(reversed(playerS))
        currentHold=0
        labelImage.configure(image=ph)
        labelRoll.configure(text='0')
    
imReset = Image.open(r'newzg1.png')
phReset = ImageTk.PhotoImage(imReset)    

buttonReset = tkinter.Button(rootzg1, image=phReset, text='New Game', foreground='green', command=new_game)
buttonReset.pack(padx=10,pady=10)

imRoll = Image.open(r'rollzg1.png')
phRoll = ImageTk.PhotoImage(imRoll)

buttonRoll = tkinter.Button(rootzg1, image=phRoll, text='Roll dice', foreground='green', command=roll_dice)
buttonRoll.pack(padx=10,pady=10)

imHold = Image.open(r'holdzg1.png')
phHold = ImageTk.PhotoImage(imHold)

buttonHold = tkinter.Button(rootzg1, image=phHold, text='Hold', foreground='green', command=hold_lol)
buttonHold.pack(padx=10,pady=10)

rootzg1.mainloop()
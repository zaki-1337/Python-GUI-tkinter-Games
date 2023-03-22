##########################################################################################################################################################################################
######  run "pip install pyimage" first! #################################################################################################################################################
##########################################################################################################################################################################################

from tkinter import *
from PIL import Image,ImageTk  #for implementing images
import random
from subprocess import call #for running other scripts from a button on the main window (another script)
import os #to get current working directory

#####################################################################
rootM = Tk()

rootM.title('PyGAMES!')
rootM.geometry('900x700')
rootM.resizable(height=False,width=False)

imBG = Image.open(r'bgMain.jpg')
phBG = ImageTk.PhotoImage(imBG)

bgLabel = Label(rootM,image=phBG)
bgLabel.place(x=0,y=0)

imBNNR = Image.open(r'bannerMain.png')
phBNNR = ImageTk.PhotoImage(imBNNR)

titleLabel = Label(rootM,image=phBNNR)
titleLabel.pack(side=TOP,pady=15)

instLabel = Label(rootM,text="Choose any of the six games you'd like to play",font=("Comic Sans",25),fg="#31dbeb",
                  bg="#9547ed")
instLabel.pack(side=TOP,pady=10)

#####################################################################

currentWorkingDir = os.getcwd()

#####################################################################

def hemGam1f():
    
    class CallPy1(object):
        
        def __init__(self,path=currentWorkingDir+"/hem1.py"):
            self.path=path
            
        def call_python1(self):
            call(["Python3","{}".format(self.path)])
            
    
    if __name__=="__main__":
        
        h1=CallPy1()
        h1.call_python1()


#####################################################################

def hemGam2f():
    
    class CallPy2(object):
        
        def __init__(self,path=currentWorkingDir+"/hem2.py"):
            self.path=path
            
        def call_python2(self):
            call(["Python3","{}".format(self.path)])
            
    
    if __name__=="__main__":
        
        h2=CallPy2()
        h2.call_python2()


#####################################################################

hemGam1=Button(rootM,text='Image here',command=hemGam1f).place(x=200,y=300)
hemGam2=Button(rootM,text='Image here',command=hemGam2f).place(x=200,y=500)

#####################################################################

def manGam1f():
    
    class CallPy3(object):
        
        def __init__(self,path=currentWorkingDir+"/ticy.py"):
            self.path=path
            
        def call_python3(self):
            call(["Python3","{}".format(self.path)])
            
    
    if __name__=="__main__":
        
        m1=CallPy3()
        m1.call_python3()


#####################################################################

def manGam2f():
    
    class CallPy4(object):
        
        def __init__(self,path=currentWorkingDir+"/snek.py"):
            self.path=path
            
        def call_python4(self):
            call(["Python3","{}".format(self.path)])
            
    
    if __name__=="__main__":
        
        m2=CallPy4()
        m2.call_python4()
    

#####################################################################

manGam1=Button(rootM,text='Image here',command=manGam1f).place(x=400,y=300)
manGam2=Button(rootM,text='Image here',command=manGam2f).place(x=400,y=500)

#####################################################################

def zakGam1f():
    
    class CallPy5(object):
        
        def __init__(self,path=currentWorkingDir+"/PigGame.py"):
            self.path=path
            
        def call_python5(self):
            call(["Python3","{}".format(self.path)])
            
    
    if __name__=="__main__":
        
        z1=CallPy5()
        z1.call_python5()


#####################################################################
   
def zakGam2f():
    
    class CallPy6(object):
        
        def __init__(self,path=currentWorkingDir+"/GuessGame.py"):
            self.path=path
            
        def call_python6(self):
            call(["Python3","{}".format(self.path)])
            
    
    if __name__=="__main__":
        
        z2=CallPy6()
        z2.call_python6()


#####################################################################

zakGam1=Button(rootM,text='Image here',command=zakGam1f).place(x=600,y=300)
zakGam2=Button(rootM,text='Image here',command=zakGam2f).place(x=600,y=500)

rootM.mainloop()
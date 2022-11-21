from tkinter import *
from PIL import ImageTk, Image
import random
root = Tk()
root.geometry("1000x1000")
root.title("Game")
f1=Frame(root,bg='grey',height="150",width='500')
f1.pack(fill=X)
l1=Label(f1,text="Rock,Paper & Scissors ",font="Centaur 30",fg='red')
l1.place(x=350,y=15)
l1=Label(f1,text="Game ",font="Centaur 30",fg='red')
l1.place(x=470,y=65)
#body
f2=Frame(root,bg='cyan',height=1000)
f2.pack(fill=BOTH)
Label(f2,text='Your choice',bg='cyan',font=25,padx=10).place(x=70,y=10)
Label(f2,text='Computer choice',bg='cyan',font=25,padx=10).place(x=720,y=10)

#for message
msg=Label(f2,text='',bg='cyan',font=35)
msg.place(x=410,y=50)

#to update result
choice=['rocks','paper','scissor']
global score
#for rock
def rockf():
    compchoice=choice[random.randint(0,2)]
    if compchoice=='rocks':
        compimg.configure(image=rocks)
    elif compchoice=='paper':
        compimg.configure(image=paper)
    else:
        compimg.configure(image=scissor)
    userimg.configure(image=rocks)
    if compchoice=='rocks':
        msg['text']='Tie'
    elif compchoice=='scissor':
        msg['text']='You Won'
        score=int(userscore['text'])
        score+=1
        userscore['text']=score
    else:
        msg['text']='You Lost'
        score = int(compscore['text'])
        score += 1
        compscore['text'] = score
#for paper
def paperf():
    compchoice=choice[random.randint(0,2)]
    if compchoice=='rocks':
        compimg.configure(image=rocks)
    elif compchoice=='paper':
        compimg.configure(image=paper)
    else:
        compimg.configure(image=scissor)
    userimg.configure(image=paper)
    if compchoice=='paper':
        msg['text']='Tie'
    elif compchoice=='rocks':
        msg['text']='You Won'
        score=int(userscore['text'])
        score+=1
        userscore['text']=score
    else:
        msg['text']='You Lost'
        score = int(compscore['text'])
        score += 1
        compscore['text'] = score
#for scissor
def scissorf():
    compchoice=choice[random.randint(0,2)]
    if compchoice=='rocks':
        compimg.configure(image=rocks)
    elif compchoice=='paper':
        compimg.configure(image=paper)
    else:
        compimg.configure(image=scissor)
    userimg.configure(image=scissor)
    if compchoice=='scissor':
        msg['text']='Tie'
    elif compchoice=='paper':
        msg['text']='You Won'
        score=int(userscore['text'])
        score+=1
        userscore['text']=score
    else:
        msg['text']='You Lost'
        score = int(compscore['text'])
        score += 1
        compscore['text'] = score


#for score
f3=Frame(f2,bg='yellow',height=100,width=200)
f3.place(x=400,y=200)
userscore=Label(f3,text=0,bg='yellow',width=7)
compscore=Label(f3,text=0,bg='yellow',width=7)
userscore.grid(row=1,column=0)
compscore.grid(row=1,column=2)

#for images
rocks=ImageTk.PhotoImage(Image.open('rock.jpg'))
paper=ImageTk.PhotoImage(Image.open('paper.jpg'))
scissor=ImageTk.PhotoImage(Image.open('scissors.jpg'))
userimg=Label(f2,image=scissor,width=200,height=300,bg='cyan')
compimg=Label(f2,image=paper,width=200,height=300,bg='cyan')
userimg.place(x=20,y=100)
compimg.place(x=700,y=100)

#for buttons
Label(f2,text='Select your choice',bg='cyan',font='comicsans 15',fg='green').place(x=390,y=400)
r1=Button(f2,text='Rock',bg='red',command=rockf,width=10)
r2=Button(f2,text='Paper',bg='red',command=paperf,width=10)
r3=Button(f2,text='Scissor',bg='red',command=scissorf,width=10)
r1.place(x=350,y=450)
r2.place(x=430,y=450)
r3.place(x=510,y=450)
root.mainloop()

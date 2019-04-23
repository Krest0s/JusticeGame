from tkinter import *
import random

massive=[]
category = ['Страна','Столица','Правитель']

def openfile():
    f=open('massive.txt')
    for i in range():
        a=[f.readline(),f.readline(),f.readline()]
        massive.insert(i, a)
    f.close()
    for i in range(5):
        for j in range(3):
            massive[i][j] = massive[i][j].replace('\n', '')

def country():
    if massive[0]==[]:
        text.delete(1.0, END)
        text.insert(1.0,'Игра окончена!')
    else:
        i=random.randint(0,len(massive[0])-1)
        ra=massive[0].pop(i)
        del massive[1][i]
        del massive[2][i]
        text.delete(1.0, END)
        text.insert(1.0,'Cлучайная страна - ')
        text.insert(2.0,ra)
        text.insert(3.0,'\n')

def capital():
    if massive[1]==[]:
        text.delete(1.0, END)
        text.insert(1.0,'Игра окончена!')
    else:
        i=random.randint(0,len(massive[1])-1)
        ra=massive[1].pop(i)
        del massive[0][i]
        del massive[2][i]
        text.delete(1.0, END)
        text.insert(1.0, 'Cлучайная страна - ')
        text.insert(2.0, ra)
        text.insert(3.0, '\n')

def ruler():
    if massive[2]==[]:
        text.delete(1.0, END)
        text.insert(1.0,'Игра окончена!')
    else:
        i=random.randint(0,len(massive[2])-1)
        ra=massive[2].pop(i)
        del massive[0][i]
        del massive[1][i]
        text.delete(1.0, END)
        text.insert(1.0, 'Cлучайная страна - ')
        text.insert(2.0, ra)
        text.insert(3.0, '\n')

openfile()
root = Tk()
root.title("Justice Game")
root.geometry("640x640")
w=10
h=1
s='left'
x=50
frame = Frame(relief=RAISED, borderwidth=1,height=1)
text = Text(font='16')
text.pack()
frame.pack(fill=BOTH, expand=True)
btn1 = Button(text=category[0], background="white", foreground="black", width=w, height=h, font="16", command=country,padx=x)
btn1.pack(side=s)
btn2 = Button(text=category[1], background="white", foreground="black", width=w, height=h, font="16", command=capital,padx=x)
btn2.pack(side=s)
btn3 = Button(text=category[2], background="white", foreground="black", width=w, height=h, font="16", command=ruler,padx=x)
btn3.pack(side=s)
label = Label()
label.pack()
root.mainloop()

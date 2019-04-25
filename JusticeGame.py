from tkinter import *
import random

massive=[]
category = ['Страна','Столица','Правитель']

def openfile():
    f=open('massive.txt')
    for i in range(3):
        a = []
        for j in range(5):
            a.insert(j,f.readline())
        massive.insert(i, a)
    f.close()
    for i in range(3):
        for j in range(5):
            massive[i][j] = massive[i][j].replace('\n', '')

def country():
    if massive[0]==[]:
        label_var.set('Игра окончена!')
    else:
        i=random.randint(0,len(massive[0])-1)
        ra=massive[0].pop(i)
        del massive[1][i]
        del massive[2][i]
        label_var.set('Случайная страна - ' + ra)
        label.update()

def capital():
    if massive[1]==[]:
        label_var.set('Игра окончена!')
    else:
        i=random.randint(0,len(massive[1])-1)
        ra=massive[1].pop(i)
        del massive[0][i]
        del massive[2][i]
        label_var.set('Случайная столица - ' + ra)
        label.update()

def ruler():
    if massive[2]==[]:
        #text.delete(1.0, END)
        label_var.set('Игра окончена!')
    else:
        i=random.randint(0,len(massive[2])-1)
        ra=massive[2].pop(i)
        del massive[0][i]
        del massive[1][i]
        label_var.set('Случайный правитель - ' + ra)
        label.update

openfile()

root = Tk()
root.title("Justice Game")
root.iconbitmap('icon.ico')
root.geometry("640x640")
w=10
h=1
s='top'
x=50

label_var = StringVar()
label = Label(root, font='40', bg="white", width=100, height=13, textvariable=label_var)
label.pack()

btn1 = Button(text=category[0], background="white", foreground="black", width=w, height=h, font="16", command=country,padx=x)
btn1.pack(side=s)
btn2 = Button(text=category[1], background="white", foreground="black", width=w, height=h, font="16", command=capital,padx=x)
btn2.pack(side=s)
btn3 = Button(text=category[2], background="white", foreground="black", width=w, height=h, font="16", command=ruler,padx=x)
btn3.pack(side=s)
root.mainloop()

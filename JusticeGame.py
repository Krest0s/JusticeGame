from tkinter import *
import random


massive=[]                  #в этом массиве будет все хранится
clever=[]                    #массив для самых умных
category = ['Термин','Определение','Вопрос на засыпку(слишком умный?)']             #названия кнопок
n=148      #количество примеров в категории


def openfile():
    f=open('massive.txt')
    for i in range(2):
        a = []
        for j in range(n):
            a.insert(j,f.readline())
        massive.insert(i, a)
    for i in range(2):
        for j in range(n):
            massive[i][j] = massive[i][j].replace('\n', '')
    f.close()

    c=open('smart.txt')
    for i in range(2):
        a = []
        for j in range(24):
            a.insert(j,c.readline())
        clever.insert(i, a)
    for i in range(2):
        for j in range(24):
            clever[i][j] = clever[i][j].replace('\n', '')
    c.close()



def otvet():
    if  r==0:
        text.delete(1.0, END)
        text.insert(1.0, 'Ответ - ')
        text.insert(2.0, massive[1][i])
        del massive[1][i]
    elif r==1:
        text.delete(1.0, END)
        text.insert(1.0, 'Ответ - ')
        text.insert(2.0, massive[0][i])
        del massive[0][i]
    elif r==2:
        text.delete(1.0, END)
        text.insert(1.0, 'Ответ - ')
        text.insert(2.0, clever[0][i])
        del clever[0][i]

def termin():
    if massive[0]==[]:
        text.delete(1.0, END)
        text.insert(1.0, 'Игра окончена!')
    else:
        global r, i
        i=random.randint(0,len(massive[0])-1)
        ra=massive[0].pop(i)
        text.delete(1.0, END)
        text.insert(1.0, 'Что такое - ')
        text.insert(2.0, ra)
        text.insert(3.0, '?')
        r=0
    return r,i

def opred():
    if massive[1]==[]:
        text.delete(1.0, END)
        text.insert(1.0, 'Игра окончена!')
    else:
        global i, r
        i=random.randint(0,len(massive[1])-1)
        ra=massive[1].pop(i)
        text.delete(1.0, END)
        text.insert(1.0, 'Что такое - ')
        text.insert(2.0, ra)
        text.insert(3.0, '?')
        r=1
    return r, i

def smart():
    if clever[1]==[]:
        text.delete (1.0, END)
        text.insert (1.0, 'Вопросы для умных кончились!')
    else:
        global r, i
        i=random.randint(0,len(clever[1])-1)
        ra=clever[1].pop(i)
        text.delete(1.0, END)
        text.insert(1.0, 'Вопрос - ')
        text.insert(2.0, ra)
        r=2
    return r,i

openfile()

root = Tk()
root.title("Justice Game")
root.iconbitmap('icon.ico')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
w=9
h=1
s='top'
x=170 #длина кнопок
y=1
f='Arial 20' #шрифт кнопок

text = Text(font='Arial 40', height=7, width=50)
text.pack()
text.insert(1.0, 'Привет, сейчас мы проверим, как вы знакомы с правом.\nЧтобы начать играть выберите термин, определение, или вопрос для самых умных.\nУдачи!\n\nИгра создана: vk.com/unkn0w_npers0n\n                        vk.com/georgy_ivanov2018')

btn1 = Button(text=category[0], background="white", foreground="black", width=w, height=h, font=f, command=termin,padx=x, pady=y)
btn1.pack(side=s)
btn2 = Button(text=category[1], background="white", foreground="black", width=w, height=h, font=f, command=opred,padx=x, pady=y)
btn2.pack(side=s)
btn3 = Button(text=category[2], background="white", foreground="black", width=w, height=h, font=f, command=smart,padx=x, pady=y)
btn3.pack(side=s)
btn4 = Button(text='Ответ', background="white", foreground="black", width=w, height=h, font=f, command=otvet, padx=x, pady=y)
btn4.pack(side=s)

root.mainloop()

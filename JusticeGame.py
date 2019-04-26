from tkinter import *
import random
from tkinter.scrolledtext import ScrolledText
massive=[]                  #в этом массиве будет все хранится
category = ['Термин','Определение','Вопрос на засыпку(слишком умный?)']
n=7      #количество примеров в категории


def openfile():
    f=open('massive.txt')
    for i in range(3):
        a = []
        for j in range(n):
            a.insert(j,f.readline())
        massive.insert(i, a)
    f.close()
    for i in range(3):
        for j in range(n):
            massive[i][j] = massive[i][j].replace('\n', '')

def otvet():
    if  r==0:
        #label_var.set('Ответ - ' + massive[1][i])
        #label.update()
        text.delete(1.0, END)
        text.insert(1.0, 'Ответ - ')
        text.insert(2.0, massive[1][i])
        del massive[1][i]
    elif r==1:
        #label_var.set('Ответ - ' + massive[0][i] + '\n')
        #label.update()
        text.delete(1.0, END)
        text.insert(1.0, 'Ответ - ')
        text.insert(2.0, massive[0][i])
        del massive[0][i]


def termin():
    if massive[0]==[]:
        text.delete(1.0, END)
        text.insert(1.0, 'Игра окончена!')
    else:
        global r, i
        i=random.randint(0,len(massive[0])-1)
        ra=massive[0].pop(i)
        text.delete(1.0, END)
        text.insert(1.0, 'Термин - ')
        text.insert(2.0, ra)
        '''label_var.set('Термин - ' + ra)
        label.update()'''
        r=0
    return r,i


def opred():
    if massive[1]==[]:
        label_var.set('Игра окончена!')
    else:
        global i, r
        i=random.randint(0,len(massive[1])-1)
        ra=massive[1].pop(i)
        text.delete(1.0, END)
        text.insert(1.0, 'Определение - ')
        text.insert(2.0, ra)
        '''label_var.set('Определение - ' + ra)
        label.update()'''

        r=1
    return r, i



def vidotn():
    if massive[2]==[]:
        label_var.set('Игра окончена!')
    else:
        global r, i
        i=random.randint(0,len(massive[2])-1)
        ra=massive[2].pop(i)
        text.delete(1.0, END)
        text.insert(1.0, 'Вопрос - ')
        text.insert(2.0, ra)
        '''label_var.set(ra)
        label.update()'''
        r=2
    return r,i

openfile()

root = Tk()
#root.attributes('-fullscreen', True)
root.title("Justice Game")
root.iconbitmap('icon.ico')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#use the next line if you also want to get rid of the titlebar
root.geometry("%dx%d+0+0" % (w, h))
#root.geometry("fullscreen")
w=9
h=1
s='top'
x=170 #длина кнопок
y=1
f='Arial 20' #шрифт кнопок

'''label_var = StringVar()
label = Label(root, font='Calibri 20', bg="white", width=100, height=13, textvariable=label_var)
label.pack()'''
text = Text(font='Arial 40', height=7)
text.pack()

btn1 = Button(text=category[0], background="white", foreground="black", width=w, height=h, font=f, command=termin,padx=x, pady=y)
btn1.pack(side=s)
btn2 = Button(text=category[1], background="white", foreground="black", width=w, height=h, font=f, command=opred,padx=x, pady=y)
btn2.pack(side=s)
btn3 = Button(text=category[2], background="white", foreground="black", width=w, height=h, font=f, command=vidotn,padx=x, pady=y)
btn3.pack(side=s)
btn4 = Button(text='Ответ', background="white", foreground="black", width=w, height=h, font=f, command=otvet, padx=x, pady=y)
btn4.pack(side=s)
root.mainloop()

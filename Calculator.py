"""
Author@ Md. Abdur Rouf.
I have built a Calculator in Python GUI. It works very well and runs fast desktop applications.
Apr 2019 – Jun 2019
"""
from  tkinter import *
import math
root = Tk()
root.title("Calculator built by Rouf")
root.geometry("380x550+200+100")
root.resizable(False,False)
def enterNumber(x):
    if entry_box.get() == '0':
       if x == '.':
          entry_box.insert(1,'0.')
       entry_box.delete(0,'end')
       entry_box.insert(0,str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length,str(x))

def funClear():
    entry_box.delete(0,END)
    entry_box.insert(0,'0')
result = 0
history = []
def funcOperator():
    content = entry_box.get()
    result = eval(content)
    entry_box.delete(0, END)
    entry_box.insert(0,result)
    history.append(content)
    history.reverse()

    status.configure(text="History: " + ' | '.join(history[:4]),font="verdana 10 bold")

def funcDelete():
    length = len(entry_box.get())
    entry_box.delete(length-1,'end')
    if length == 1:
        entry_box.insert(0,"0")


#----entryBox------------------------------------
entry_box = Entry(font='verdana 14 bold',width=22,bd=6, justify=RIGHT,bg="#e6e6fa")
entry_box.insert(0,'0')
entry_box.place(x=30,y=10)
#----------number button------------------------------
btn_number = []
for i in range(10):
    btn_number.append(Button(width=4, text=str(i),bd=6,command=lambda x = i:enterNumber(x)))

btn_txt = 1
for i in range (0,3):
    for j in range(0,3):
        btn_number[btn_txt].place(x=30+j*90, y=70+i*70)
        btn_txt+=1

btn_zero = Button(width=4, text='0',bd=6, command= lambda x = 0:enterNumber(x))
btn_zero.place(x=30,y=280)

btn_dot = Button(width=4, text='.',bd=6, command= lambda x = '.':enterNumber(x))
btn_dot.place(x=120,y=280)

btn_del = Button(width=4, text='del',bd=6, command = funcDelete )
btn_del.place(x=212,y=280)

btn_clear = Button(width=9, text='C',font="verdana 14 bold", bd=4, command = funClear)
btn_clear.place(x=30,y=340)

btn_equal = Button(width=9, text='=',font="verdana 14 bold", bd=3, command = funcOperator)
btn_equal.place(x=220,y=340)


#------------operator button-----------------
def enter_Operator(x):
    if entry_box.get() != "0":
        length=len(entry_box.get())
        all_text = entry_box.get()
        last_char = all_text[-1:]
        if last_char in ['+','-','/'] or all_text[-2:]=="**":
            pass
        else:
            entry_box.insert(length, btn_operator[x]['text'])

btn_operator =[]
for i in range(4):
    btn_operator.append((Button(width=4,font="verdana 12 bold",bd=4,command = lambda x = i:enter_Operator(x))))

btn_operator[0]['text'] = '+'
btn_operator[1]['text'] = '-'
btn_operator[2]['text'] = '*'
btn_operator[3]['text'] = '/'

for i in range(4):
    btn_operator[i].place(x=290, y=70+i*70)


status = Label(root, text="History: ", relief=SUNKEN, height=3, anchor=W, font="verdana 11 bold")
status.pack(side=BOTTOM, fill=X)

root.mainloop()
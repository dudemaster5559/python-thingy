print("hello world")

from tkinter import *
from gtts import gTTS
from playsound import playsound
from tkinter import scrolledtext

root = Tk()
root.geometry("450x400")
root.resizable(0, 0)
root.configure(bg='ghost white')
root.title("TEXT TO SPEECH")

L1 = Label(root, text="TEXT_TO_SPEECH", font="arial 15 bold",
           fg="#20bebe", bg='white smoke').pack()

L2 = Label(root, text="Enter Text", font='arial 10 bold',
           bg='white smoke').place(x=20, y=60)


Msg = StringVar()


textareaframe = Frame(root)
textareaframe.pack()
textareaframe.place(x=20, y=80)

TextArea = Text(textareaframe, textvariable=Msg)
ScrollBar = Scrollbar(textareaframe)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set, width=40, height=10)
ScrollBar.pack(side=RIGHT, fill=Y)
TextArea.pack()

def Convert():
    Message = TextArea.get()
    speech = gTTS(text=Message)
    speech.save('T2S.mp3')
    playsound('T2S.mp3')


def Play():
    pass


def Exit():
    root.destroy()


def Reset():
    Msg.set("")


buttonframe = Frame(root)
buttonframe.pack(padx=5, pady=5)
buttonframe.place(y=280)

Button(buttonframe, text="Convert", font='arial 14 bold',
       command=Convert).pack(side=LEFT, padx=5)

Button(buttonframe, text="PLAY", font='arial 14 bold',
       command=Play).pack(side=LEFT, padx=5)

Button(buttonframe, text='EXIT', font='arial 14 bold',
       command=Exit, bg="#20bebe").pack(side=LEFT, padx=5)

Button(buttonframe, text='RESET', font='arial 14 bold',
       command=Reset).pack(side=LEFT, padx=5)


L_end = Label(text="SAAD QURESHI", font='arial 12 bold', fg="#20bebe",
              bg='white smoke', width='20').pack(side='bottom')

root.mainloop()

name = input("what is your name? type here --> ")
print("hello " + name)
birth_year = input("what year were you born?  ")
age = 2023 - int(birth_year)
print("you are",age,"years old")
q1 = input("do pineapples belong on pizzas?  ")
if q1 == "yes":
    print("next please enter password")
else:
    print("isaac d snuts")

password ="0418"

for i in range(3):
    pwd = input("Enter Password ")
    if(pwd==password):
        print("WLCOME TO THIS WEBSITE")
        break
    else:
        print("INCORRECT PASSWORD")
        continue
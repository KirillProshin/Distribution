from tkinter import *
import distribution

def output(event):
    txt = entry.get('1.0', 'end')
    a = entry3.get()
    b = entry2.get()
    c = entry1.get()
    #print(txt)
    distribution.distribution(txt,b,a,c)

    label4 = Label(window, text="Выполнено!",font=("Arial Bold", 20))
    label4.grid(column=2, row=8)

window = Tk()

window.title("Distribution")
window.geometry('600x500')

entry3 =Entry(window,width=20)
entry2 = Entry(window,width=66)
entry1 = Entry(window,width=66)
entry = Text(width=50, height=21, bg="darkgreen", fg='white', wrap=WORD)
button = Button(window, text='Разослать',bg="black", fg="red",height=5,font=("Arial Bold", 25))
label = Label(window, text='Введите id своей группы',font=("Arial Bold", 10))
label1 = Label(window, text='Введите токен своей группы',font=("Arial Bold", 10))
label2 = Label(window, text='Введите токен своего приложения',font=("Arial Bold", 10))
label3 = Label(window, text='Введите сообщение рассылки',font=("Arial Bold", 10))

label.grid(column=1, row=1)

entry3.grid(column=1, row=2)

label1.grid(column=1, row=3)

entry2.grid(column=1, row=4)

label2.grid(column=1, row=5)

entry1.grid(column=1, row=6)

label3.grid(column=1, row=7)

entry.grid(column=1, row=8)

button.grid(column=2, row=8)

button.bind('<Button-1>', output)

window.mainloop()


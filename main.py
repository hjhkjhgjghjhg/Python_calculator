from tkinter import * # Импортируем tkinter

def logicalc(operation):
    if operation == 'C':
        lbl['text'] = ''
    elif operation == 'DEL':
        lbl['text'] = lbl['text'][0:-1]
    elif operation == 'X^2':
        lbl['text'] = str(eval(lbl['text']) ** 2)  # (2 + 2) X^2
    elif operation == '=':
        lbl['text'] = str(eval(lbl['text']))
    else:
        if lbl['text'] == '0':
            lbl['text'] = ''
        lbl['text'] = lbl['text'] + operation

root = Tk() # Создание окна tkinter
root.geometry('485x550') # Размер окна 485x550 пикселей
root.title('Калькулятор') # Название приложения
root['bg'] = 'black' # Задний фон приложения -> черный
root.resizable(False, False) # Запрет на изменение размера окна пользователем
lbl = Label(root, text='0', font=('Consolas', 21, 'bold'),
            bg='black', fg='white')
lbl.place(x=11, y=50) # Распаковываем и размещаем виджет label по абсолютным координатам.
btns = ['C', 'DEL', '*', '=',
        '1', '2', '3', '/',
        '4', '5', '6', '+',
        '7', '8', '9', '-',
        '(', '0', ')', 'X^2'
        ] # Создаем список с содержанием названия будущих кнопок.
x = 10 # Координата первой кнопки по x
y = 140 # Координата первой кнопки по y
for bt in btns:
    def com(x=bt):
        logicalc(x) # Передаем аргумент-значение содержания кнопки в функцию logicalc
    Button(text=bt, bg='white', font=('Consolas', 15), command=com).place(x=x, y=y, width=115, height=79)
    x += 117 # При создании следующих кнопок в одной строчке - размещаем их на 117px правее.
    if x > 400: # Если создали 4 кнопки, то следующие будут на новой строчке
        x = 10
        y += 81

root.mainloop() # Основной цикл, отвечающий за отображение всеъ элементов tkinter

from tkinter import *

def logicalc(operation):
    if operation == 'C':
        lbl['text'] = '0'
    elif operation == 'DEL':
        lbl['text'] = lbl['text'][0:-1]
    elif operation == 'X^2':
        lbl['text'] = str(eval(lbl['text']) ** 2)
    elif operation == '=':
        lbl['text'] = str(eval(lbl['text']))
    else:
        if lbl['text'] == '0':
            lbl['text'] = ''
        lbl['text'] = lbl['text'] + operation


root = Tk()
root.geometry('485x550')
root.title('Калькулятор')
root['bg'] = 'black'
root.resizable(False, False)
lbl = Label(text='0', font=('Consolas', 21, 'bold'), bg='black', fg='white')
lbl.place(x=11, y=50)
btns = [
        'C', 'DEL', '*', '=',
        '1', '2', '3', '/',
        '4', '5', '6', '+',
        '7', '8', '9', '-',
        '(', '0', ')', 'X^2'
]
x = 10
y = 140
for bt in btns:
    def com(x=bt):
        logicalc(x)
    Button(text=bt, bg='white', font=('Consolas', 15), command=com).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 10
        y += 81
root.mainloop()
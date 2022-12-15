from tkinter import *
import pyperclip
import random

root = Tk()
root.title("Генератор паролей")
root.geometry("400x200")

print("Password generation")

passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def genetate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']

    password = ""

    for x in range(passlen.ger()):
        password = password + random.choise(pass1)

    passstr.set(password)

def copytoclipboard():
    random_password = passstr.ger()
    pyperclip.copy(random_password)

Label(root, text="Приложение - генераторй паролей", font="calibri 20 bold").pack()

Label(root, text="Введите длину пароля").pack(pady=3)

Entry(root, textvariable=passlen).pack(pady=3)

Button(root, text="Создать пароль", command=genetate).pack(pady=3)

Entry(root, textvariable=passstr).pack(pady=3)

Button(root, text="Копировать в буфер обмена", command=copytoclipboard).pack()

root.mainloop()
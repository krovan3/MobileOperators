from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import tkinter.font as font
import time

defaultpadx = 10
defaultpady = 15
defaultwidth = 20
info = ["ФИО: ", "Серия паспорта: ", "Номер паспорта: ", "Регистрация: ", "Дата рождения: ", "Пол: ", "Номер: ", " Баланс: ", "Тариф","Id Абонента: " ]
con = sqlite3.connect("baza.db")
cursor = con.cursor()


def mainfunc(reg2, entryabo, entrynum, entrytarif, entrybal):
    abonent = entryabo.get()
    num = entrynum.get()
    tarif = entrytarif.get()
    balance = entrybal.get()
    a = con.execute(f"SELECT subscriber FROM numbers WHERE number=={num}")
    for line in a:
        if not line[0]:
            con.execute(
                f"UPDATE numbers SET subscriber = {abonent}, tarif = {tarif}, balance = {balance} where number = {num}")
            con.commit()
            messagebox.showinfo("Успешно", "Абонент успешно зарегистрирован")
            reg2.destroy()
        else:
            messagebox.showerror("Ошбика", "Данный номер уже зарегистрирован")


def mainfuncwindow():
    reg2 = Tk()
    reg2.geometry('300x150')
    reg2.config(background="#faebd7")
    countrow = 0
    labelfabo = ttk.Label(reg2, background='#ffe4c4', text="Id Абонента")
    labelfabo.grid(row=countrow, column=0)
    entryabo = ttk.Entry(reg2, background='#ffe4c4')
    entryabo.grid(row=countrow, column=1)
    countrow = countrow + 1
    labelnum = ttk.Label(reg2, background='#ffe4c4', text="Номер телефона")
    labelnum.grid(row=countrow, column=0)
    entrynum = ttk.Entry(reg2, background='#ffe4c4')
    entrynum.grid(row=countrow, column=1)
    countrow = countrow + 1
    labeltarif = ttk.Label(reg2, background='#ffe4c4', text="Номер тарифа")
    labeltarif.grid(row=countrow, column=0)
    entrytarif = ttk.Entry(reg2, background='#ffe4c4')
    entrytarif.grid(row=countrow, column=1)
    countrow = countrow + 1
    labelbal = ttk.Label(reg2, background='#ffe4c4', text="Первоначальный баланс")
    labelbal.grid(row=countrow, column=0)
    entrybal = ttk.Entry(reg2, background='#ffe4c4')
    entrybal.grid(row=countrow, column=1)
    countrow = countrow + 1
    label = ttk.Label(reg2, background='#faebd7', text="")
    label.grid(row=countrow, column=0)
    butsubmit = ttk.Button(reg2, text="Зарегистрировать",
                           command=lambda: mainfunc(reg2, entryabo, entrynum, entrytarif, entrybal))
    butsubmit.grid(row=countrow + 2, column=0, columnspan=2)


def id():
    if entrypassport1.get() and entrypassport2.get() and len(entrypassport1.get()) == 4 and len(entrypassport2.get()) == 6:
        series = entrypassport1.get()
        num = entrypassport2.get()
        a = con.execute(f"SELECT FIO,Id FROM subscribers WHERE passport_num == {num} and passport_series == {series}")
        lines = a.fetchone()
        if lines:
            messagebox.showinfo("",f"У абонента {lines[0]} id - {lines[1]}")
        else:
            messagebox.showerror("", f"Данный пользователь не найден ")
    else:
        messagebox.showerror("", f"Введите корректные паспортные данные")


def register():
    reg = Tk("cringe")
    reg.geometry('250x250')
    countrow = 0
    reg.resizable(height='false', width='false')
    reg.configure(background='#faebd7')
    labelfio = ttk.Label(reg, background='#ffe4c4', text=info[countrow])
    labelfio.grid(row=countrow, column=0)
    entryfio = ttk.Entry(reg, background='#ffe4c4')
    entryfio.grid(row=countrow, column=1)
    countrow = countrow + 1
    labelpasportser = ttk.Label(reg, background='#ffe4c4', text=info[countrow])
    labelpasportser.grid(row=countrow, column=0)
    entrypasportser = ttk.Entry(reg, background='#ffe4c4')
    entrypasportser.grid(row=countrow, column=1)
    countrow = countrow + 1
    labelpasportsnum = ttk.Label(reg, background='#ffe4c4', text=info[countrow])
    labelpasportsnum.grid(row=countrow, column=0)
    entrypasportnum = ttk.Entry(reg, background='#ffe4c4')
    entrypasportnum.grid(row=countrow, column=1)
    countrow = countrow + 1
    labelregister = ttk.Label(reg, background='#ffe4c4', text=info[countrow])
    labelregister.grid(row=countrow, column=0)
    entryregister = ttk.Entry(reg, background='#ffe4c4')
    entryregister.grid(row=countrow, column=1)
    countrow = countrow + 1
    labelDoB = ttk.Label(reg, background='#ffe4c4', text=info[countrow])
    labelDoB.grid(row=countrow, column=0)
    entryDoB = ttk.Entry(reg, background='#ffe4c4')
    entryDoB.grid(row=countrow, column=1)
    countrow = countrow + 1
    labelsex = ttk.Label(reg, background='#ffe4c4', text=info[countrow])
    labelsex.grid(row=countrow, column=0)
    entrysex = ttk.Entry(reg, background='#ffe4c4')
    entrysex.grid(row=countrow, column=1)
    countrow = countrow + 1
    butsubmit = ttk.Button(reg,text="Зарегистрировать",command=lambda: registraciya(reg,entrypasportser, entrypasportnum, entryregister, entryDoB, entrysex, entryfio))
    butsubmit.grid(row=countrow+1, column=0, columnspan=2)


def registraciya(reg,entrypasportser,entrypasportnum,entryregister,entryDoB,entrysex,entryfio):
    passer = entrypasportser.get()
    pasnum = entrypasportnum.get()
    regist = entryregister.get()
    dob = entryDoB.get()
    sex = entrysex.get()
    FIO = entryfio.get()
    try:
        valid_date = time.strptime(dob, '%d.%m.%Y')
    except:
        messagebox.showerror("", "Некорректная дата (Введите в формате дд.мм.гггг)")
        reg.destroy()
        return 0
    if len(passer) == 4:
        if len(pasnum) == 6:
            if regist:
                if sex == "М" or sex == "Ж":
                    for x in FIO:
                        if x.isspace() or x.isalpha():
                            pass
                        else:
                            messagebox.showerror("", "Введите ФИО верно!")
                            reg.destroy()
                            return 0
                        a = con.execute(f"SELECT * FROM subscribers WHERE passport_series == {passer}  and passport_num =={pasnum}")
                        if a.fetchall():
                            messagebox.showerror("","Такой абонент уже зарегистрирован")
                            reg.destroy()
                            return 0
                        else:
                            con.execute(f"INSERT INTO subscribers(passport_series, passport_num, registration, date_of_birth, sex, fio) VALUES({passer},{pasnum},\'{regist}\', \'{dob}\', \'{sex}\', \'{FIO}\')")
                            con.commit()
                            b = con.execute(f"SELECT * FROM subscribers WHERE passport_series == {passer} and passport_num =={pasnum}")
                            line = b.fetchall()
                            messagebox.showinfo("", f"Абонент {FIO} успешно зарегистрирован. Id - {line[0]}")
                            reg.destroy()
                            return 0
                else:
                    messagebox.showerror("", "Введите пол верно!")
                    reg.destroy()
                    return 0
            else:
                messagebox.showerror("", "Введите регистрацию!")
                reg.destroy()
                return 0
        else:
            messagebox.showerror("", "Введите номер паспорта верно!")
            reg.destroy()
            return 0
    else:
        messagebox.showerror("", "Введите серию паспорта верно!")
        reg.destroy()
        return 0
    con.commit()


def emptycheck():
    emptychecker = Tk("cringe")
    emptychecker.geometry('1100x400')
    framedannie = Frame(emptychecker)
    framedannie.pack(side=LEFT)
    framedannie.config(bg='#faebd7')
    framenomera = Frame(emptychecker)
    framenomera.pack(side=RIGHT)
    framenomera.config(bg='#faebd7')
    emptychecker.configure(background='#faebd7')
    entryrempty = ttk.Entry(framedannie, width=40)
    entryrempty.grid(row=0, column=0, padx=10)
    buttonrepleniempty = ttk.Button(framedannie, text="Кончается на", command=lambda: emptycheckercommand(framenomera, "%"+entryrempty.get()))
    buttonrepleniempty.grid(row = 1, column= 0)
    buttonrepleniempty = ttk.Button(framedannie, text="Начинается на", command=lambda: emptycheckercommand(framenomera, entryrempty.get()+"%"))
    buttonrepleniempty.grid(row=2, column=0)
    buttonrepleniempty = ttk.Button(framedannie, text="Содержит", command=lambda: emptycheckercommand(framenomera, "%"+entryrempty.get()+"%"))
    buttonrepleniempty.grid(row=3, column= 0)


def emptycheckercommand(framenomera,num):
    for widget in framenomera.winfo_children():
        widget.destroy()
    a = con.execute(f"SELECT number FROM numbers WHERE numbers.number like \'{num}\' and numbers.subscriber is Null")
    countrow = 0
    countcol = 1
    for line in a.fetchall():
        labels = ttk.Label(framenomera, text=line[0])
        labels.grid(row=countrow, column=countcol, padx=20, pady=defaultpady)
        countcol = countcol + 1
        if countcol % 9 == 0:
            countrow = countrow + 1
            countcol = countcol - 8


def replenish(balance,sum):
    sum = float(sum)
    a = con.execute(f"UPDATE numbers set balance = balance+ {sum} where number = {balance}")
    con.commit()
    messagebox.showinfo("Успех",f"Баланс пополнен на {sum} рублей")


def test(button):
    number = button["text"]
    a = con.execute(f"SELECT FIO,passport_series,passport_num,registration,date_of_birth,sex,number,balance,tarifs.name,subscribers.Id FROM numbers,subscribers,tarifs WHERE numbers.number == {number} and numbers.subscriber == subscribers.Id and tarifs.id == numbers.tarif")
    checker = a.fetchall()
    if checker:
        sub = Tk("cringe")
        sub.resizable(height='false',width='false')
        sub.configure(background='#faebd7')
        countrow = 0
        for row in checker:
            for i in range(len(info)):
                labelfionum = ttk.Label(sub, background='#ffe4c4', text=info[i])
                labelfionum.grid(row=countrow, column=0)
                labelfionum = ttk.Label(sub,background='#ffe4c4', text=row[i])
                labelfionum.grid(row=countrow ,column=1)
                countrow = countrow + 1

            entryreplenish = ttk.Entry(sub, width=15)
            entryreplenish.grid(row=countrow+1, column=0, padx=0, pady=defaultpady)

            buttonreplenish = ttk.Button(sub, text="Пополнить баланс", command=lambda: replenish(row[6],entryreplenish.get()))
        buttonreplenish.grid(row=countrow + 1, column=1)
    else:
        messagebox.showerror("Ошибка", f"Номер не зарегистрирован")


def check():
    for widget in framecringe.winfo_children():
        widget.destroy()
    if entryFIO.get():
        FIO = entryFIO.get()
        FIO = "%" + FIO + '%'
        a = con.execute(f"SELECT * FROM numbers,subscribers WHERE subscribers.FIO like \'{FIO}\'and numbers.subscriber==subscribers.Id")
        countrow = 0
        countcol = 3
        for line in a.fetchall():
            button = ttk.Button(framecringe, text=line[0])
            button.config(command=lambda button=button: test(button))
            button.grid(row=countrow, column=countcol, padx=20, pady=defaultpady)
            countcol = countcol + 1
            if countcol % 3 == 0:
                countrow = countrow+1
                countcol = countcol - 3
    elif entrypassport1.get() and entrypassport2.get() and len(entrypassport1.get()) == 4 and len(entrypassport2.get()) == 6:
        pasportser = entrypassport1.get()
        pasportnum = entrypassport2.get()
        a = con.execute(f"SELECT * FROM numbers,subscribers WHERE subscribers.passport_num == \'{pasportnum}\' and subscribers.passport_series ==\'{pasportser}\' and numbers.subscriber==subscribers.Id")
        countrow = 0
        countcol = 3
        i = 0
        for line in a.fetchall():
            button = ttk.Button(framecringe, text=line[0], command=lambda:test(["text"]))
            button.config(command=lambda button=button: test(button))
            button.grid(row=countrow, column=countcol, padx=20, pady=defaultpady)
            countcol = countcol + 1
            i = i + 1
            if (countcol) % 3 == 0:
                countrow = countrow + 1
                countcol = countcol - 3
    elif entrynumber.get():
        nomer = entrynumber.get()
        a = con.execute(f"SELECT * FROM numbers WHERE numbers.number like \'{nomer}\'")
        countrow = 0
        countcol = 3
        for line in a.fetchall():
            button = ttk.Button(framecringe, text=line[0])
            button.config(command=lambda button=button: test(button))
            button.grid(row=countrow, column=countcol, padx=20, pady=defaultpady)
            countcol = countcol + 1
            if countcol% 3 == 0:
                countrow = countrow + 1
                countcol = countcol - 3
    else:
        messagebox.showerror("error", "Введите данные")


root = Tk("maifdsfdsfn")
root.title("Курсовая Ваньков")
root.geometry("925x400")

font2 = font.Font(family="Segoe UI ", size=20, weight="normal", slant="roman")

framebut = Frame(root)
framebut.pack(side=BOTTOM, fill="x")
framebut.config(background="#faebd7")

framevivod = Frame(root)
framevivod.pack(side=LEFT)
framevivod.config(bg = '#faebd7')

framecringe = Frame(root)
framecringe.pack(side=RIGHT)
framecringe.config(background='#faebd7')

frameids = Frame(root)
frameids.pack(side=RIGHT)
frameids.config(background='#faebd7')


root.configure(background='#faebd7')
labelFIO = ttk.Label(framevivod, background='#ffe4c4', text="ФИО:")
labelFIO.config(font=("Segoe UI", 20))
labelFIO.grid(row=0, column=0, padx=defaultpadx, pady=defaultpady)
labelpassport = ttk.Label(framevivod, background='#ffe4c4', text="Паспорт:")
labelpassport.config(font=("Segoe UI", 20))
labelpassport.grid(row=1, column=0, padx=defaultpadx, pady=defaultpady)

labelnumber = ttk.Label(framevivod,background='#ffe4c4', text="Номер телефона:")
labelnumber.config(font=("Segoe UI", 20))
labelnumber.grid(row=2, column=0, padx=defaultpadx, pady=defaultpady)

entryFIO = ttk.Entry(framevivod,width=15)
entryFIO.grid(row=0, column=1, padx=0, pady=defaultpady, sticky="w", columnspan=2)

entrypassport1 = ttk.Entry(framevivod, width=15)
entrypassport1.grid(row=1, column=1, sticky="w", pady=defaultpady)
entrypassport2 = ttk.Entry(framevivod)
entrypassport2.grid(row=1, column=2, sticky="w", padx=0, pady=defaultpady)
entrynumber = ttk.Entry(framevivod,width=15)
entrynumber.grid(row=2, column=1, sticky="w", padx=0, pady=defaultpady)
entry1 = ttk.Entry()
# entry1.grid(row=0,column=1,padx=defaultpadx,pady=defaultpady)
# labelnumber = ttk.Label(text="Номер телефона:").grid(row=2,column=0,padx=defaultpadx,pady=defaultpady)
btnFinder = Button(framebut, text="Поиск", command=lambda: [check()], height=4,width=25)
btnFinder.grid(columnspan=2, row=0,column=0)
btnempty = Button(framebut, text="Проверка доступности номера",command =lambda:[emptycheck()],height=4,width=25)
btnempty.grid(columnspan=2, column=2,row=0)
btnreg = Button(framebut, text="Регистрация пользователя",command =lambda:[register()],height=4,width=25)
btnreg.grid(columnspan=2, column=4,row=0)
btnid = Button(framebut, text="Узнать ID абонента",command =lambda:[id()],height=4,width=25)
btnid.grid(columnspan=2, column=6,row=0)
btnregnum = Button(framebut, text="Регистрация номера",command=mainfuncwindow,height=4,width=25)
btnregnum.grid(columnspan=2, column=8,row=0)
# label2 = ttk.Label().grid(row=3, column=0,padx=defaultpadx,pady=defaultpady,columnspan=2)

root.mainloop()

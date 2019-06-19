#!/usr/bin/python3

def write_number(number):
    number_monitor.insert('end',number)

def delete_number():
    numlen = len(number_monitor.get(0.0,'end'))-2
    number_monitor.delete('1.{}'.format(numlen))

def number_clear():
    numlen = len(number_monitor.get(0.0,'end'))-1
    for i in range(00,numlen):
        number_monitor.delete('0.0')

def jam_numbers():
    global number1
    global char
    number1 = int(number_monitor.get(0.0,'end'))
    number_clear()
    char = '+'

def menha_number():
    global number1
    global char
    number1 = int(number_monitor.get(0.0,'end'))
    number_clear()
    char = '-'

def zarb_number():
    global number1
    global char
    number1 = int(number_monitor.get(0.0,'end'))
    number_clear()
    char = '*'

def taghsim_number():
    global number1
    global char
    number1 = int(number_monitor.get(0.0,'end'))
    number_clear()
    char = '/'

def mosavi():
    global number1
    global number2
    global char   
    number2 = int(number_monitor.get(0.0,'end'))
    if char == '+':
        sum_numbers = number1 + number2
        number_clear()
        number_monitor.insert('end',sum_numbers)

    elif char == '-':
        sum_numbers = number1 - number2
        number_clear()
        number_monitor.insert('end',sum_numbers)

    elif char == '*':
        sum_numbers = number1 * number2
        number_clear()
        number_monitor.insert('end',sum_numbers)

    elif char == '/':
        sum_numbers = number1 / number2
        number_clear()
        number_monitor.insert('end',sum_numbers)


number1 = 0
number2 = 0
char = ''

import tkinter as tk
from tkinter import ttk

#create main window
root = tk.Tk()
root.geometry('250x350')
root.title('Calculater')
root.config(bg='black')

#create monitor text
number_monitor = tk.Text(root,width=25,height=5,bg='black',fg='white',relief='ridge',bd=20)
number_monitor.grid(row=0,column=0,columnspan=6)

#create butttons
btn_clear = tk.Button(root,text='C',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='red',command=lambda: number_clear())
btn_clear.grid(row=1,column=0)

btn_jam = tk.Button(root,text='+',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='red',command=lambda: jam_numbers())
btn_jam.grid(row=1,column=1)

btn_menha = tk.Button(root,text='-',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='red',command=lambda: menha_number())
btn_menha.grid(row=1,column=2)

btn_zarb = tk.Button(root,text='‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍×',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='red',command=lambda: zarb_number())
btn_zarb.grid(row=3,column=3)

btn_taghsim = tk.Button(root,text='‍÷',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='red',command=lambda: taghsim_number())
btn_taghsim.grid(row=2,column=3)

btn_delete = tk.Button(root,text='‍Del',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='red',command=lambda: delete_number())
btn_delete.grid(row=1,column=3)

btn_mosavi = tk.Button(root,text='‍=',width=14,height=1,font=('Tahoma','18'),bg='#10100F',fg='red',command=lambda: mosavi())
btn_mosavi.grid(row=5,column=0,columnspan=6)

#btn numbers
btn_one = tk.Button(root,text='1',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(1))
btn_one.grid(row=2,column=0)

btn_two = tk.Button(root,text='2',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(2))
btn_two.grid(row=2,column=1)

btn_three = tk.Button(root,text='3',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(3))
btn_three.grid(row=2,column=2)

btn_four = tk.Button(root,text='4',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(4))
btn_four.grid(row=3,column=0)

btn_five = tk.Button(root,text='5',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(5))
btn_five.grid(row=3,column=1)

btn_six = tk.Button(root,text='6',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(6))
btn_six.grid(row=3,column=2)

btn_seven = tk.Button(root,text='7',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(7))
btn_seven.grid(row=4,column=0)

btn_eight = tk.Button(root,text='8',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(8))
btn_eight.grid(row=4,column=1)

btn_nine = tk.Button(root,text='9',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(9))
btn_nine.grid(row=4,column=2)

btn_zero = tk.Button(root,text='0',width=2,height=1,font=('Tahoma','18'),bg='#10100F',fg='blue',command=lambda: write_number(0))
btn_zero.grid(row=4,column=3)

root.mainloop()
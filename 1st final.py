#myPfunProject#

from tkinter import *
import random

def dice():

    def roll():
        Dice1=random.randint(1,6)
        Dice2=random.randint(1,6)
        number1.set(Dice1)
        number2.set(Dice2)
        print()
        

    window=Toplevel()
    window.iconbitmap("ico.ico")
    window["bg"]="black"
    window.title("Dice Roller")
    window.geometry("450x520")     
    
    
    number1=StringVar()
    number2=StringVar()
    number01=Entry(window,text=number1)
    number02=Entry(window,text=number2)
    number1.set("Dice 1")
    number2.set("Dice 2")


    background=PhotoImage(file="logo.GIF")
    Label(window,image=background,bd=0).pack()
    
    bt1=Button(window,text="Roll",fg="blue",bg="grey",command=roll,height="2",width="5")
    bt1.place(x=215,y=400)
    number01.pack()
    number02.pack()

    window.mainloop()


def sim_cal():
    window=Toplevel()
    window.geometry("323x210")
    window.title("Simple Calculator")
    window.iconbitmap("symbo.ico")
    window["bg"]="black"
    
    entry_value=StringVar()
    
    def click_button(number):
        global expression
        expression=expression+number
        entry_value.set(expression)
        
    def equal_button():
        global expression,answer
        expression=str(eval(expression))
        answer=str(round(eval(expression),3))
        entry_value.set(expression)
        expression=""
        
    def clear_button():
        global expression
        expression=""
        entry_value.set(expression)
    
    def delete_button():
        global expression
        exp_list=list(expression)
        del exp_list[-1]
        expression="".join(exp_list)
        entry_value.set(expression)
    
    def answer_button():
        global expression,answer
        expression=expression+answer
        entry_value.set(expression)
    
    
    entry=Entry(window,textvariable=entry_value)
    entry_value.set("Enter Expression")
    entry.grid(columnspan=5, ipadx=100, pady=10)
    
    button0=Button(window, command=lambda:click_button("0"),text="0",bg="blue",fg="white",height=2, width=7)
    button0.grid(row=5, column=0)
    
    button1=Button(window, command=lambda:click_button("1"),text="1",bg="blue",fg="white",height=2, width=7)
    button1.grid(row=2, column=0)
    
    button2=Button(window, command=lambda:click_button("2"),text="2",bg="blue",fg="white",height=2, width=7)
    button2.grid(row=2, column=1)
    
    button3=Button(window, command=lambda:click_button("3"),text="3",bg="blue",fg="white",height=2, width=7)
    button3.grid(row=2, column=2)
    
    button4=Button(window, command=lambda:click_button("4"),text="4",bg="blue",fg="white",height=2, width=7)
    button4.grid(row=3, column=0)
    
    button5=Button(window, command=lambda:click_button("5"),text="5",bg="blue",fg="white",height=2, width=7)
    button5.grid(row=3, column=1)
    
    button6=Button(window, command=lambda:click_button("6"),text="6",bg="blue",fg="white",height=2, width=7)
    button6.grid(row=3, column=2)
    
    button7=Button(window, command=lambda:click_button("7"),text="7",bg="blue",fg="white",height=2, width=7)
    button7.grid(row=4, column=0)
    
    button8=Button(window, command=lambda:click_button("8"),text="8",bg="blue",fg="white",height=2, width=7)
    button8.grid(row=4, column=1)
    
    button9=Button(window, command=lambda:click_button("9"),text="9",bg="blue",fg="white",height=2, width=7)
    button9.grid(row=4, column=2)
    
    plus=Button(window, command=lambda:click_button("+"),text="+",bg="yellow",height=2, width=7)
    plus.grid(row=2, column=3)
    
    minus=Button(window, command=lambda:click_button("-"),text="-",bg="yellow",height=2, width=7)
    minus.grid(row=3, column=3)
    
    multiply=Button(window, command=lambda:click_button("*"),text="x",bg="yellow",height=2, width=7)
    multiply.grid(row=4, column=3)
    
    divide=Button(window, command=lambda:click_button("/"),text="/",bg="yellow",height=2, width=7)
    divide.grid(row=5, column=3)
    
    power=Button(window, command=lambda:click_button("**"),text="^",bg="blue",fg="white",height=2, width=7)
    power.grid(row=5, column=1)
    
    decimal=Button(window, command=lambda:click_button("."),text=".",bg="blue",fg="white",height=2, width=7)
    decimal.grid(row=5, column=2)
    
    equal=Button(window, command=lambda:equal_button(), text="=",bg="yellow",height=2, width=7)
    equal.grid(row=2, column=4)
    
    clear=Button(window, command=lambda:clear_button(), text="Clear",bg="yellow",height=2, width=7)
    clear.grid(row=4, column=4)
    
    delete=Button(window, command=lambda:delete_button(), text="Del",bg="yellow",height=2, width=7)
    delete.grid(row=5, column=4)
    
    ans=Button(window, command=lambda:answer_button(), text="Ans",bg="yellow",height=2, width=7)
    ans.grid(row=3, column=4)

expression=""
answer=""

window=Tk()
window.title("Python Projects")
window.iconbitmap("pytho.ico")
window["bg"]="grey"
window.geometry("500x350")
background=PhotoImage(file="V1.gif")

label=Label(window,image=background)
calculator_button=Button(window, text="Simple Calculator",bg="gold",fg="black",command=sim_cal)
dice_button=Button(window, text="Simple Roller",bg="RoyalBlue3",fg="black",command=dice)

label.pack()
calculator_button.place(x=40,y=150)
dice_button.place(x=355,y=150)
window.mainloop()


    

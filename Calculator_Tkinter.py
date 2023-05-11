from tkinter import *
import winsound
import threading
import time


def PlayS():                      #We define the function
    winsound.Beep(999, 99)        #Using winsound module to play a sound

def b_cl(num):                               #We define the function
    threading.Thread(target=PlayS).start()      #Running the function designed for sound, it plays a sound when a button is clicked
    current_num = entry_box.get()       #We save the first entry into a variable
    entry_box.delete(0, END)            #Clear the entry box so we can add another number or sign afterwards
    entry_box.insert(0, str(current_num)+str(num))  #Insert the current number and the next numbber/character together


def b_clear():                                  #We define the function
    threading.Thread(target=PlayS).start()      #Running the function designed for sound, it plays a sound when a button is clicked
    entry_box.delete(0, END)        #Delete the whole content of the box


def b_del_click():                          #We define the function
    threading.Thread(target=PlayS).start()      #Running the function designed for sound, it plays a sound when a button is clicked
    entry_box.delete(len(entry_box.get())-1, END)   #Delete only the last character inserted


def b_calculate():                          #We define the function
    result = eval(str(entry_box.get()))     #Takes the whole content of the box as a string, and using eval it calculates it and store it into a variable
    entry_box.delete(0, END)                #It clears the whole content of the box
    entry_box.insert(0, result)             #Insert the result

def b_equal():                                  #We define the function
    thread1 = threading.Thread(target=PlayS)        #Running the function designed for sound, it plays a sound when a button is clicked
    thread2 = threading.Thread(target=b_calculate)      #Running the calculate function to get the result
    thread1.start()     #Starts the first thread
    time.sleep(0.1)     #Wait for 0.1 seconds
    thread2.start()     #Starts the second thread


root = Tk()         #Initialize the main widget
root.title("Python_Calculator")     #Title for root
root.geometry("370x300")            #Sizes for root window


entry_box = Entry(root, width=50, borderwidth=4)            #Creating the entry box
entry_box.grid(row=0, column=0, columnspan=6, padx=11, pady=11) #Attach it to the main window

b_del = Button(root, text="<x", padx=5, pady=4, command=b_del_click)            #Creating the delete button
b_1 = Button(root, text="1", padx=15, pady=10, command=lambda: b_cl(1))      #Creating nr 1 button
b_2 = Button(root, text="2", padx=15, pady=10, command=lambda: b_cl(2))      #Creating nr 2 button
b_3 = Button(root, text="3", padx=15, pady=10, command=lambda: b_cl(3))      #Creating nr 3 button
b_4 = Button(root, text="4", padx=15, pady=10, command=lambda: b_cl(4))      #Creating nr 4 button
b_5 = Button(root, text="5", padx=15, pady=10, command=lambda: b_cl(5))      #Creating nr 5 button
b_6 = Button(root, text="6", padx=15, pady=10, command=lambda: b_cl(6))      #Creating nr 6 button
b_7 = Button(root, text="7", padx=15, pady=10, command=lambda: b_cl(7))      #Creating nr 7 button
b_8 = Button(root, text="8", padx=15, pady=10, command=lambda: b_cl(8))      #Creating nr 8 button
b_9 = Button(root, text="9", padx=15, pady=10, command=lambda: b_cl(9))      #Creating nr 9 button
b_0 = Button(root, text="0", padx=15, pady=10, command=lambda: b_cl(0))      #Creating nr 0 button
b_add = Button(root, text="+", padx=15, pady=10, command=lambda: b_cl("+"))  #Creating + button
b_sub = Button(root, text="-", padx=15, pady=10, command=lambda: b_cl("-"))  #Creating - button
b_mult = Button(root, text="x", padx=15, pady=10, command=lambda: b_cl("*")) #Creating * button
b_div = Button(root, text="/", padx=15, pady=10, command=lambda: b_cl("/"))  #Creating / button
b_clear = Button(root, text="C", padx=15, pady=10, command=b_clear)             #Creating clear button
b_equal = Button(root, text="=", padx=30, pady=10, command=b_equal)             #Creating = button
b_dot = Button(root, text=".", padx=15, pady=10, command=lambda: b_cl("."))  #Creating . button
b_par1 = Button(root, text="(", padx=15, pady=10, command=lambda: b_cl("(")) #Creating ( button
b_par2 = Button(root, text=")", padx=15, pady=10, command=lambda: b_cl(")")) #Creating ) button


b_clear.grid(row=1, column=1, sticky="nsew")    #Attaching clear button
b_par1.grid(row=1, column=2, sticky="nsew")     #Attaching ( button
b_par2.grid(row=1, column=3, sticky="nsew")     #Attaching ) button
b_0.grid(row=5, column=1, sticky="nsew")        #Attaching 0 button
b_dot.grid(row=5, column=2, sticky="nsew")      #Attaching . button
b_equal.grid(row=5, column=3, sticky="nsew", columnspan=2)  #Attaching = button
b_1.grid(row=4, column=1, sticky="nsew")        #Attaching nr 1 button
b_2.grid(row=4, column=2, sticky="nsew")        #Attaching nr 2 button
b_3.grid(row=4, column=3, sticky="nsew")        #Attaching nr 3 button
b_4.grid(row=3, column=1, sticky="nsew")        #Attaching nr 4 button
b_5.grid(row=3, column=2, sticky="nsew")        #Attaching nr 5 button
b_6.grid(row=3, column=3, sticky="nsew")        #Attaching nr 6 button
b_7.grid(row=2, column=1, sticky="nsew")        #Attaching nr 7 button
b_8.grid(row=2, column=2, sticky="nsew")        #Attaching nr 8 button
b_9.grid(row=2, column=3, sticky="nsew")        #Attaching nr 9 button
b_add.grid(row=4, column=4, sticky="nsew")      #Attaching + button
b_sub.grid(row=3, column=4, sticky="nsew")      #Attaching - button
b_mult.grid(row=2, column=4, sticky="nsew")     #Attaching * button
b_div.grid(row=1, column=4, sticky="nsew")      #Attaching / button
b_del.grid(row=0, column=6)                     #Attaching delete button


root.mainloop()     #Method to run our window

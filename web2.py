# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:29:27 2019

@author: admin
"""
import sys
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import * 
from tkinter.scrolledtext import ScrolledText
window = Tk()


window.title("Web Presence Finder Tool")
 
window.geometry('2000x2000')
scrollbar = Scrollbar(window)
txt = Entry(window, width=25)
txt.grid(column=0, row=1)





 
try: 
    
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
    
    
def out():
    global txt,window
    
    problem = str(txt.get())

    print(problem)
    
# to search 
    list1=[]
    for j in search(problem, tld="co.in", num=10, stop=100, pause=2): 
        list1.append(j)
    print(list1)
    str1= ''
    for i in range(0,len(list1)):
        l1 = Label(window,text = str(len(list1[i])))
        l1 = Label(window,text = list1[i])
        
        l1.grid(row=i+6,column=0)
    
    for l in range(1):
        
        file = open('filename.text' + str(l), 'w')
        file.write(str(list1))
        file.write(str(len(list1)))
        
        file.close()

    
btn = Button(window, text="Search", width=15, command=out)
btn.grid(column=0, row=3)


window.mainloop()


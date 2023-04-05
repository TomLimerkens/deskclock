#from tkinter import *
import tkinter as tk
import math 
from datetime import datetime
import time

#create main window
mainwindow = tk.Tk()
mainwindow.title("MyGui")
mainwindow.geometry("1920x400")

# #Create label
# label = tk.Label(mainwindow, text="HelloWorld")

# #draw window
# label.pack()

# #create Canvas
# panel = tk.Canvas(mainwindow, width = 400, height = 400)
# panel.pack()

# panel.create_line(0,0,300,300)
# panel.create_line(0,100,100,0, 
#                   fill="red", 
#                   dash=(8,3))

# panel.create_rectangle(50,25,150,75, 
#                        fill="blue")

# panel.create_oval(100,100,300,300,
#                   fill="green", 
#                   outline="Black")


#TODO : Something goes wrong below, it is a memory leak / recurrence that should not be here.
def time_update():
    #print(f'time is is {datetime.now()}!')
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    #label.config(text=f'Counter is {datetime.now()}!')
    clock.after(1000, time_update())
    #label.pack()
#    mainwindow.after(500, mainloop())
    
clock = tk.Label(mainwindow, font=("times", 50, "bold"), bg="white")
clock.pack(fill="both", expand=True)

time_update()
#run window
mainwindow.mainloop()

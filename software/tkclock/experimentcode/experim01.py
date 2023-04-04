import time
import tkinter as tk


window = tk.Tk()
window.geometry("400x800")
bodytitle = tk.Label(text="Ola display")
bodytitle.pack()

window.mainloop()

# clode below needs multi threading
count = 0
while True:
     print("count ", count)
     count += 1
     time.sleep(.5)
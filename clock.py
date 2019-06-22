import tkinter as tk
from time import strftime


clock_frame = tk.Label()
clock_frame.pack()


# this function holds the PC current time on our frame
def tic():
 clock_frame['text'] = strftime("%H:%M:%S")
 clock_frame['font'] = 'Robotica 75 bold'
 clock_frame['fg'] = 'black'


# this function refreshes the tic() function after 1000miliseconds
def tac():
 tic()
 clock_frame.after(1000, tac)

tac()
clock_frame.mainloop()

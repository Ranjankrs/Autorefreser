#import tkinter as tk
import pyautogui as pg 
import tkinter as tk
window = tk.Tk()
window.title('refresh tool')
window.geometry("300x200+10+20")
def ref():
    pg.hotkey('win','d')
    #pg.hotkey('ctrl', 'a')
    INPUT = int(inputtxt.get("1.0", "end-1c"))
    pg.hotkey('win','d')

    for n in range(INPUT):
		# right click
        pg.hotkey('f5')
	    #pg.click( x=950, y=500, button="right")
		# left click
	    #pg.click( x=975, y=560)
	
label=tk.Label(window,text="enter number")
label.pack()
inputtxt = tk.Text(window, height = 5,
                width = 25,
                bg = "light yellow")
inputtxt.pack()
#pg.hotkey('win','d')
entry=tk.Entry(window)
b=tk.Button(window,text="click here",command= lambda:ref())
b.pack()
window.mainloop()
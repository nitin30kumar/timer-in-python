from tkinter import *
import time

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.label = Label(text="",anchor="center",justify="center",fg="red" , font=("Helvetica",20))
        self.label.place(x=240,y=150)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now,anchor="center")
        self.after(1000,self.update_clock)

root = Tk()
app = App(root)
root.wm_title("Tkinter Clock")
Label(root,text="Clock using Tkinter",fg="violet",font="jokerman 25").pack()
root.geometry("600x300")
root.after(1000,app.update_clock)
Label(text="Made with LOVE by Black Eagle",fg="blue",font="verdana 17").pack()

root.mainloop()

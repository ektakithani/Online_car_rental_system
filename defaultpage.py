import tkinter as tk
import time
from PIL import ImageTk,Image

class DefaultPage:
    def __init__(self,root):
        self.root=root
        self.f=tk.Frame(self.root,height=681,width=1024)
        self.f.pack()
        self.img = ImageTk.PhotoImage(Image.open(r"C:\Users\ektak\PycharmProjects\OCR\cars\vanshi.jpg"))
        self.panel=tk.Label(self.f,height=681,width=1024,image=self.img)
        self.panel.pack()
        self.m=tk.Message(self.f,width=1000,font="Roman 20 bold",text="CarDekho.com",relief=tk.SOLID,borderwidth=1)
        self.m.pack()
        self.m.place(x=450,y=100)
        localtime=time.asctime(time.localtime(time.time()))
        self.lblinfo=tk.Label(self.f,font=('Roman','20','bold'),text=localtime)
        self.lblinfo.place(x=80,y=100)
        self.panel.pack_propagate(0)  # donot shrink label
        self.f.pack_propagate(0)  # donot shrink frame

"""
root=tk.Tk()
d=DefaultPage(root)
root.mainloop()
"""
"""add frame
        create image
        add image to label
        add text
        to resize == reduceimages.com
        
        """

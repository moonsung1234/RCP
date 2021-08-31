
from PIL import ImageGrab
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox
import tkinter

class Screen :
    def __init__(self, w, h) :
        self.tk = tkinter
        self.window_width = w
        self.window_height = h

        # self.window = None
        # self.title_label = None
        # self.combobox = None
        # self.picture_label = None
        # self.picture = None

        self.window = Tk()
        self.window.title("Screen capture")
        self.window.geometry("%dx%d" % (self.window_width, self.window_height))
        self.window.resizable(False, False)

        self.combobox_list = []

    def addElement(self, e) :    
        self.combobox_list.append(e)

    def _postCallback(self) :
        self.combobox["value"] = self.combobox_list

    def setTitle(self, title) :
        _font = Font(family="맑은 고딕", size=30)
        self.title_label = Label(self.window, font=_font, text=title)
        self.title_label.place(x=50, y=50)

    def setCombobox(self, callback) :
        self.combobox = Combobox(self.window, width=30, height=100, state="readonly", postcommand=self._postCallback)
        self.combobox.bind("<<ComboboxSelected>>", callback)
        self.combobox.place(x=50, y=150)

    def setPicture(self) :
        _font = Font(size=20)
        self.picture_label = Label(self.window, font=_font, text="Background")
        self.picture_label.place(x=250, y=250)

        self.image = PhotoImage(file="./default.png")
        self.picture = Label(self.window, image=self.image)
        self.picture.place(x=10, y=300)

    def setProgramBar(self) :
        _font = Font(size=20)
        self.program_bar_label = Label(self.window, font=_font, text="Program")
        self.program_bar_label.place(x=780, y=250)

        self.program_bar = Text(self.window, width=40, height=27)
        self.program_bar.place(x=700, y=300)

    def updatePicture(self) :
        self.image2 = PhotoImage(file="./background.png")
        self.picture.config(image=self.image2)

    def show(self) :
        self.window.mainloop()
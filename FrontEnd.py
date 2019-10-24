# created by Kieran Jerry Jonathon
import os
import tkinter
from tkinter import *
from tkinter import filedialog


class GuiInterface:
    master = tkinter.Tk()
    canvas = tkinter.Canvas(master, bg='white', width=500, height=500)

    def __init__(self, source_reader):
        self.canvas.pack(side='bottom', fill='x', expand='yes')
        self.init_widgets()
        self.SourceReader = source_reader

    def init_widgets(self):
        self.master.title('TkinterGUI')
        width = 1200
        height = 600
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        center = '%dx%d+%d+%d' % (width, height, (screenwidth - 800) / 2, (screenheight - height) / 2)
        self.master.geometry(center)
        self.master.draw_btn = Button(self.master, text='Draw', command=self.draw)
        self.master.draw_btn.pack(side='left', fill='both', expand='yes')
        self.master.import_btn = Button(self.master, text='import', command=self.to_import)
        self.master.import_btn.pack(side='left', fill='both', expand='yes')
        self.master.instruction = Label(self.master, text='Please enter command:', font=('serif', 18))
        self.master.instruction.pack(side='left', fill='both', expand='yes')
        self.master.text = Text(self.master, height=27, width=32)
        self.master.text.pack(side='left', fill='both', expand='yes')

    def draw(self):
        self.SourceReader.parser.parse(self.master.text.get(1.0, "end-1c"))

    def insert_text(self, row_source):
        self.master.text.insert('0.0', row_source)

    def to_import(self):
        imported_file = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if imported_file is not '':
            self.insert_text(open(imported_file, "r+").read())

    def start(self):
        self.master.mainloop()

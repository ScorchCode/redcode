
import tkinter as tk
from tkinter import ttk


class Buttons(ttk.Frame):
    """A tkinter.Frame with Buttons."""
    def __init__(self, parent):
        super().__init__(master=parent)
        self.open = ttk.Button(master=self, text="Open", command=parent.open_file)
        self.clear = ttk.Button(master=self, text="Clear", command=parent.clear)
        self.done = ttk.Button(master=self, text="Done", command=parent.done)

        self.open.grid(row=0, column=0)
        self.clear.grid(row=0, column=1)
        self.done.grid(row=0, column=2)


class Editor(ttk.Frame):
    """A tkinter.Frame showing a text widget with scrollbars."""
    def __init__(self, parent):
        super().__init__(master=parent)
        self.text = tk.Text(
            self,
            width=80, height=20,
            wrap=tk.NONE,
            padx=10, pady=5,
            font="TkFixedFont"
        )
        self.scb_vertical = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.scb_horizontal = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.text.xview)

        self.text.configure(yscrollcommand=self.scb_vertical.set)
        self.text.configure(xscrollcommand=self.scb_horizontal.set)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.text.grid(row=0, column=0, sticky=tk.NSEW)
        self.scb_vertical.grid(row=0, column=1, sticky=tk.NS)
        self.scb_horizontal.grid(row=1, column=0, sticky=tk.EW)

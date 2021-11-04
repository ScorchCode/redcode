
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Post Markup Helper")

        self.frm_editor = ttk.Frame(self)
        self.txt_editor = tk.Text(
            self.frm_editor,
            width=80, height=20,
            wrap=tk.NONE,
            padx=10, pady=5
        )

        self.scb_vertical = ttk.Scrollbar(self.frm_editor, orient=tk.VERTICAL, command=self.txt_editor.yview)
        self.scb_horizontal = ttk.Scrollbar(self.frm_editor, orient=tk.HORIZONTAL, command=self.txt_editor.xview)
        self.txt_editor.configure(yscrollcommand=self.scb_vertical.set)
        self.txt_editor.configure(xscrollcommand=self.scb_horizontal.set)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frm_editor.grid_rowconfigure(0, weight=1)
        self.frm_editor.grid_columnconfigure(0, weight=1)

        self.frm_editor.grid(sticky=tk.NSEW)
        self.txt_editor.grid(row=0, column=0, sticky=tk.NSEW)
        self.scb_vertical.grid(row=0, column=1, sticky=tk.NS)
        self.scb_horizontal.grid(row=1, column=0, sticky=tk.EW)


if __name__ == "__main__":
    app = App()
    app.mainloop()

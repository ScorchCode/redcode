
import tkinter as tk
from tkinter import ttk

import frames


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reddit Codeblock Poster")

        self.editor = frames.Editor(parent=self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.editor.grid(sticky=tk.NSEW)

        self.editor.text.insert(1.0, "text")


if __name__ == "__main__":
    app = App()
    app.mainloop()

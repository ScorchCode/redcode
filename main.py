
import tkinter as tk
from tkinter import ttk

import frames


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reddit Codeblock Pasting Crutch")

        self.editor = frames.Editor(parent=self)
        self.button = frames.Buttons(parent=self)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button.grid(sticky=tk.EW)
        self.editor.grid(sticky=tk.NSEW)

    def clear(self):
        self.editor.text.delete(1.0, "end")

    def done(self):
        indent = "    "
        codeblock = indent
        for c in self.editor.text.get(1.0, "end-1c"):
            codeblock += c
            if c == "\n":
                codeblock += indent

        self.clipboard_clear()
        self.clipboard_append(codeblock)

    def from_clipboard(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()

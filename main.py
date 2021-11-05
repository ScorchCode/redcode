from pathlib import Path
import tkinter as tk
from tkinter import messagebox, filedialog

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

        messagebox.showinfo(
            title="Done",
            message="Codeblock copied to clipboard.\nPaste on Reddit\nin Markdown modus."
        )

    def open_file(self):
        textfile = Path(filedialog.askopenfilename(
            title="Open a file",
            initialdir=Path("~").expanduser()
        ))
        self.clear()
        self.editor.text.insert(1.0, textfile.read_text())


if __name__ == "__main__":
    app = App()
    app.mainloop()

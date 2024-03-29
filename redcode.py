#!/usr/bin/env python3
"""
A Python + Tkinter text editor that adds 4 spaces before every line.

Reddit's Deluxe Editor is buggy when pasting.
When pasting code in Markdown modus, a code block needs to have
4 spaces preceding every line.

Edit your code in this editor and click "Done".
Empty lines preceding and trailing your code are added.
4 leading spaces are added to every code line.
The TAB character is replaced by 4 spaces.
Your altered code gets copied to the clipboard
and can be pasted to Reddit's Markdown editor.

LICENSE: MIT
see https://github.com/ScorchCode/redcode/blob/main/LICENSE
"""

import json
import os
from pathlib import Path
import re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, TclError


class App(tk.Tk):
    """
    The main tkinter window.

    Attributes
    ----------
    editor: class Editor
        A ttk.Frame showing Text and Scrollbars
    button: class Buttons
        A ttk.Frame with Buttons
    mainmenu: class MainMenu
        Set up of a tk.Menu bar
    settingspath: pathlib.Path
        Where to find settings
    settings: dict
        User settings
    openpath: pathlib.Path
        Most recent directory to open text files from

    Methods
    -------
    about()
        Show About dialog.
    censor()
        Tag selected text as censored.
    clear()
        Delete all text from editor.
    done()
        Copy markdown formatted codeblock to clipboard.
    help()
        Show Help text.
    open_file()
        Replace current text with file content.
    """
    def __init__(self):
        super().__init__()
        self.title("Reddit Codeblock Pasting Crutch")

        self.settingspath = Path("redcode_settings.json")
        self.settings = load_settings(self.settingspath)
        self.openpath = Path(self.settings["loadfrom"])

        self.editor = Editor(parent=self)
        self.button = Buttons(parent=self)

        self.button.pack(expand=True, fill=tk.X)
        self.editor.pack(expand=True, fill=tk.BOTH)

        self.mainmenu = MainMenu(parent=self)
        self.config(menu=self.mainmenu)

    def about(self):
        lines = [
            "Reddit Codeblock Pasting Crutch",
            "A text editor that adds 4 spaces before every line.",
            "MIT License, Henning 2021",
            "https://github.com/ScorchCode/redcode"
        ]
        messagebox.showinfo("About", "\n".join(lines))
        
    def censor(self):
        try:
            self.editor.text.tag_add("censored", tk.SEL_FIRST, tk.SEL_LAST)
        except TclError:
            pass

    def clear(self):
        """Delete all text from editor."""
        self.editor.text.delete(1.0, tk.END)

    def done(self):
        """Copy markdown formatted codeblock to clipboard."""
        indent = 4 * " "

        # replace censored content
        if "censored" in self.editor.text.tag_names():
            blackend = "▒"
            censored_ranges = self.editor.text.tag_ranges("censored")  # tuple (start1, stop1, start2, ...)
            ranges = []  # rearrange to ((start1, stop1), (start2, stop2), ...)
            for i in range(0, len(censored_ranges), 2):
                ranges.append((censored_ranges[i], censored_ranges[i+1]))
            for start, stop in ranges:
                tl = len(self.editor.text.get(start, stop))
                self.editor.text.delete(start, stop)
                self.editor.text.insert(start, tl*blackend)


        # blank line + 1st loc gets indented later
        codeblock = "\n" + self.editor.text.get(1.0, tk.END).strip()


        # add indent after every line break
        codeblock = re.subn("\n", "\n"+indent, codeblock)[0]

        # replace every tab with indent
        codeblock = re.subn("\t", indent, codeblock)[0]

        # add blank line without adding indent
        codeblock += "\n"

        self.clipboard_clear()
        self.clipboard_append(codeblock)

        messagebox.showinfo(
            title="Done",
            message="Codeblock copied to clipboard.\nPaste on Reddit\nin Markdown mode."
        )

    def help(self):
        lines = [
            "See README.MD or visit",
            "https://github.com/ScorchCode/redcode"
        ]
        messagebox.showinfo("Help", "\n".join(lines))

    def open_file(self):
        """Replace current text with file content."""
        textfile = filedialog.askopenfilename(
            title="Open a file",
            initialdir=self.openpath
        )
        if textfile:
            self.openpath = Path(textfile)
            self.clear()
            self.editor.text.insert(1.0, self.openpath.read_text())
            self.settings["loadfrom"] = str(self.openpath)
            self.settingspath.write_text(json.dumps(self.settings, indent=2))


class Buttons(ttk.Frame):
    """
    A ttk.Frame with Buttons.

    The buttons call methods provided by parent.

    Attributes
    ----------
    parent: class App
    open: tkinter.Button
    clear: tkinter.Button
    done: tkinter.Button
    """
    def __init__(self, parent):
        super().__init__(master=parent)
        self.open = ttk.Button(master=self, text="Open", command=parent.open_file)
        self.clear = ttk.Button(master=self, text="Clear", command=parent.clear)
        self.undo = ttk.Button(master=self, text="Undo", command=parent.editor.text.edit_undo)
        self.redo = ttk.Button(master=self, text="Redo", command=parent.editor.text.edit_redo)
        self.done = ttk.Button(master=self, text="Done", command=parent.done)

        self.open.pack(side=tk.LEFT)
        self.clear.pack(side=tk.LEFT)
        self.undo.pack(side=tk.LEFT)
        self.redo.pack(side=tk.LEFT)
        self.done.pack(side=tk.RIGHT, padx=25)


class Editor(ttk.Frame):
    """
    A ttk.Frame showing a text widget with scrollbars.

    Attributes
    ----------
    text: ttk.Text
        The editors text widget.
    scb_vertical: ttk.Scrollbar
    scb_horizontal: ttk.Scrollbar
    """
    def __init__(self, parent):
        super().__init__(master=parent)
        self.text = tk.Text(
            self,
            width=80, height=20,
            wrap=tk.NONE,
            padx=10, pady=5,
            font="TkFixedFont",
            tabs="1c",
            undo=True
        )
        self.text.tag_configure("censored", overstrike=True)

        self.scb_vertical = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.scb_horizontal = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.text.xview)

        self.text.configure(yscrollcommand=self.scb_vertical.set)
        self.text.configure(xscrollcommand=self.scb_horizontal.set)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.text.grid(row=0, column=0, sticky=tk.NSEW)
        self.scb_vertical.grid(row=0, column=1, sticky=tk.NS)
        self.scb_horizontal.grid(row=1, column=0, sticky=tk.EW)


class MainMenu(tk.Menu):
    """The main menu bar of the app."""
    def __init__(self, parent):
        super().__init__(master=parent)

        filemenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open", command=parent.open_file)
        filemenu.add_command(label="Done", command=parent.done)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=parent.quit)

        editmenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Clear", command=parent.clear)
        editmenu.add_separator()
        editmenu.add_command(label="Censor", command=parent.censor)
        editmenu.add_separator()
        editmenu.add_command(label="Undo", command=parent.editor.text.edit_undo)
        editmenu.add_command(label="Redo", command=parent.editor.text.edit_redo)

        helpmenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="Help", command=parent.help)
        helpmenu.add_command(label="About", command=parent.about)


def load_settings(filepath):
    """
    Load settings from json file.

    Parameters
    ----------
    filepath: pathlib.Path
        Where to find redcode_settings.json

    Returns
    -------
    dict
    """
    try:
        sett = json.loads(filepath.read_text())
    except FileNotFoundError:
        sett = {"loadfrom": str(Path.home())}
        filepath.write_text(json.dumps(sett, indent=2))
    return sett


def main():
    os.chdir(Path(__file__).parent)

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

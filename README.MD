# Reddit Codeblock Pasting Crutch
A Python + Tkinter text editor that adds 4 spaces before every line.

Reddit's Deluxe Editor is buggy when pasting.
When using Markdown modus, a codeblock needs to have
4 spaces preceding every line.

Insert and edit your code here and click "Done".
Your code, including the extra spaces as well as empty lines before and after,
gets copied to the clipboard and can be pasted to Reddit's Markdown editor.

# Requirements
Python 3.4+

# Installation
Move the script file to a directory in your `$PATH` and give permission to run as a program.

    user@machine:~/Downloads$ mv redcode.py ~/.local/bin
    user@machine:~/Downloads$ chmod +x ~/.local/bin/redcode.py

Run by calling from command line.

## How to use
* Enter text you want to insert as codeblock on Reddit.
* Do some editing (optional).
* Click "Done" to copy formatted code to clipboard.
* Paste in Reddit's Markdown modus.

## Entering text
* Type everything from scratch or
* Copy & Paste existing code or
* Load file contents by clicking "Open".

# Disclaimer
Runs on my Linux machine, but that's as far as testing went.

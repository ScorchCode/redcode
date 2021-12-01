# Reddit Codeblock Pasting Crutch
A Python + Tkinter text editor that adds 4 spaces before every line.

Reddit's Deluxe Editor is buggy when pasting. When using Markdown modus, a code block needs to have 4 spaces preceding every line.

Edit your code in this editor and click "Done".

* Empty lines preceding and trailing your code are added.
* 4 leading spaces are added to every code line.
* The TAB character is replaced by 4 spaces.

Your altered code gets copied to the clipboard and can be pasted to Reddit's Markdown editor.

![redcode](https://user-images.githubusercontent.com/47459835/140605211-73c25937-57bb-4d03-82d6-8999a261ff89.png)

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
* Click "Done" to copy re-formatted code to clipboard.
* Paste in Reddit's Markdown modus.

## Entering text
* Type everything from scratch or
* Copy & Paste existing code or
* Load file contents by clicking "Open".

# Disclaimer
Runs on my Linux machine, but that's as far as testing went.

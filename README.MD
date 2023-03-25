# Reddit Codeblock Pasting Crutch
A Python + Tkinter text editor that adds 4 spaces before every line.

Reddit's Deluxe Editor is buggy when pasting. Markdown mode works better, but an extra 4-space-indentation needs to precede every line. Or you prepare your code in this editor and click "Done".

* Empty lines preceding and trailing your code are added.
* 4 leading spaces are added to every code line.
* The TAB character is replaced by 4 spaces.

Your altered code gets copied to the clipboard and can be pasted into Reddit's Markdown editor.

![redcode2](https://user-images.githubusercontent.com/47459835/144369082-ffac8535-2a84-475b-b910-645a364963b3.png)

# Requirements
Python 3.4+

# Installation
Move the script file to a directory in your `$PATH` and give permission to run as a program.

    user@machine:~/Downloads$ mv redcode.py ~/.local/bin/redcode
    user@machine:~/Downloads$ chmod +x ~/.local/bin/redcode
    user@machine:~/Downloads$ 
    user@machine:~/Downloads$ # Run by calling from command line.
    user@machine:~/Downloads$ redcode
    user@machine:~/Downloads$ 
    
Installation on Windows may differ.

## How to use
* Enter text you want to insert as codeblock on Reddit.
* Do some editing (optional).
* Click "Done" to copy re-formatted code to clipboard.
* Paste in Reddit's Markdown mode.

## Entering text
* Type everything from scratch or
* Copy & Paste existing code or
* Load file contents by clicking "Open".

TABs can't be set to a fixed number of characters. Their width is 1 cm here, but they will have 4 spaces after copying.

## Censor text
Sensitive information can be censored. Select text and click `Edit > Censor`. Text appears strikethrough and is blackened before being copied to clipboard.

Issues: For now, there's no option to de-censor text. Also, censored text spanning multiple lines will remove the line break.

## Open a file
Search for a file to open, starting in the most recent directory.

# Disclaimer
Runs on my Linux machine, but that's as far as testing went.

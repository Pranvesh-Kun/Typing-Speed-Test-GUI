import tkinter as tk
from tkinter import ttk, END, messagebox
import time

wordlist = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', 'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now']


def start():
    entry.focus()
    global time_start
    time_start = time.time()
    words.config(state="normal")
    words.delete(1.0, END)
    for i in wordlist:
        words.insert(END, f"{i} ")


def timer(event):
    if time_start > 0:
        if time.time() <= time_start + 63:
            pass
        else:
            words.delete('1.0', '2.0')
            words.insert(index=1.0, chars="Time's up!")
            chars = 0
            for i in score:
                chars += len(i)
            messagebox.showinfo("Time's Up!", f"Your Gross WPM is: {chars/5}\n\nYour Net WPM is: {round((chars/5)-words_wrong, 2)}\n\nYour accuracy is: {(((chars/5)-words_wrong)/(chars/5))*100}%")


def detect(event):
    global score
    global words_wrong
    global number
    word = entry.get()
    entry.delete(0, END)
    words.config(state="normal")
    if word.strip() == wordlist[number]:
        score += word.strip()
        for i in range(len(word.strip())+1):
            words.delete('1.0')
        number += 1
    else:
        for i in range(len(wordlist[number]) + 1):
            words.delete('1.0')
        number += 1
        words_wrong += 1


def restart():
    global score, number, words_wrong, total_char
    score, number, words_wrong, total_char = [], 0, 0, 0
    start()


time_start = 0.0
score = []
number = 0
words_wrong = 0
total_char = 0
window = tk.Tk()
window.geometry("400x250")
window.minsize(400, 250)
window.maxsize(400, 250)
window.title("Typing Speed Test")

words = tk.Text(height=6, width=30)
words.focus()
words.insert(END, "Click the 'Start' Button to   start! You will have to type  for one minute straight.")
words.config(state="disabled")
words.grid(column=0, row=0, pady=30, columnspan=3, padx=73)

frame = ttk.Frame(window)

entry = ttk.Entry(frame)
entry.grid(column=1, row=1)
entry.focus()

button1 = ttk.Button(frame, text="Start", width=10, command=start)
button1.grid(column=0, row=1, padx=20)

button2 = ttk.Button(frame, text="Restart", width=9, command=restart)
button2.grid(column=2, row=1, padx=20)

frame.grid(row=1, column=0, columnspan=2, padx=30)

entry.bind('<space>', detect)
entry.bind('<KeyPress>', timer)


window.mainloop()

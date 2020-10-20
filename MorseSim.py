from tkinter import *

import time
import random
import threading

code, over = [], 0
free_label = "You Can Start Typing, Text Will Appear Here.\n(Use grey button or enter key...)"
CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '!': '–--.', '?': '..--..',
        '\'': '.----.', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
        '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
        ' ': ' '}


def control(spin0, keypress, screen0, text_var0, screen1):
    global row0, line0
    row0, line0 = 1, 0

    def ch_color():
        global line0
        start = "{}.{}".format(row0, line0)
        end = "{0}+1c".format(start)
        if custom_bool:  # '1.8', '1.8+1c'            change_color(txt, start, end)
            integer = len(screen0["text"]) - 1
            screen1.config(state="normal")
            try:
                if screen0["text"][-1] == screen1.get("0.0", END)[integer]:
                    screen1.tag_add("match_g", start, end)  # '1.8', '1.8+1c'
                    screen1.tag_config("match_g", background="green2")
                else:
                    screen1.tag_add("match_r", start, end)
                    screen1.tag_config("match_r", background="red")
                screen1.config(state="disabled")
                line0 += 1
            except:
                pass

    def add_char(text_var00, screen00):
        global over, letter, line0, r
        over, code_d, list0 = -1, [], ''.join(code)
        del code[:]

        for letter, code0 in CODE.items():
            code_d.append(code0)
            if code0 == list0:
                text_var00.set(screen00['text'] + letter)
    
        if list0 not in code_d:
            text_var00.set(screen00['text'] + '?')
        if not stop_event.is_set():
            text_var00.set(screen00['text'] + ' ')

    def last_abc(arg, stop_event0):
        for i in range(4):
            if not stop_event0.is_set():
                time.sleep(0.3)
                
        if not stop_event0.is_set():
            add_char(text_var0, screen0)
            change_color = threading.Thread(target=ch_color)
            change_color.start()

    def press(event):
        try:
            stop_event.set()
        except:
            pass
        
        global r, line0
        global t, dot, dash
        global TBPOC, TBC, TBW
        
        wpm = int(spin0.get())

        T = (12 / wpm) / 10  # T is one dit-time in milliseconds.
        dot, dash = T, 3 * T
        TBPOC = T    # Time Between Parts of Character = x
        TBC = 3 * T  # Time Between Character = 3x
        TBW = 7 * T  # Time Between Words = 7x

        if over == 0:
            text_var0.set("")
        elif over > 0:
            oo = time.time() - over
            if oo >= TBC:
                add_char(text_var0, screen0)
                change_color = threading.Thread(target=ch_color)
                change_color.start()
            if oo >= TBW + 0.07:
                if not r:
                    line0 += 1
                    text_var0.set(screen0["text"] + " ")
                r = False
                change_color = threading.Thread(target=ch_color)
                change_color.start()
        t = time.time()

    def release(event):
        global over, thread0, stop_event
        tt = time.time() - t

        if tt >= dash:
            code.append("-")
        elif dash > tt >= dot:
            code.append(".")
        elif tt <= dot:
            code.append(".")
        over = time.time()
        stop_event = threading.Event()
        thread0 = threading.Thread(target=last_abc, args=(1, stop_event))
        thread0.start()

    keypress.bind("<ButtonPress-1>", press)
    keypress.bind("<ButtonRelease-1>", release)
    root.bind("<KeyPress-Return>", press)
    root.bind("<KeyRelease-Return>", release)


def random_text1():
    global over, r
    global custom_bool, line0
    del code[:]
    line0, over, r, custom_bool = 0, 0, True, True
    current["text"] = "Current Section: Custom text"
    screen.config(state='normal')
    screen.delete("0.0", END)
    with open("random_sentences.txt", "r") as rr:
        read = rr.read().split("\n")
        random_sentence = random.choice(read).upper()
    screen.insert("0.0", random_sentence)
    screen.config(state="disabled")
    vvv_1.set("")


def custom_text1():
    global custom_bool

    def clear1():
        entry_3.delete(1.0, END)

    def insert():
        global row0, line0
        row0, line0 = 1, 0

        current["text"] = "Current Section: Custom text"
        screen.config(state="normal")
        screen.delete("0.0", END)
        output = ''
        for i in entry_3.get("1.0", END).split("\n"):
            output += f"{i.upper()} "
        screen.insert("0.0", output)
        screen.config(state="disabled")
        vvv_1.set(")
        custom.destroy()
        try_a()

    custom_bool = True
    custom = Tk()
    custom.geometry("655x155")
    
    Label(custom, text="Write text down here:").place(x=4, y=4)
    entry_3 = Text(custom, height=7, width=80)
    entry_3.place(x=4, y=35)
    Button(custom, text="Clear", command=clear1, width=8).place(x=510, y=4)
    Button(custom, text="Enter", command=insert, width=8).place(x=580, y=4)
    custom.mainloop()


def free_pad1():
    global over, code
    global custom_bool
    global row0, line0
    custom_bool = False
    row0, line0, over = 1, 0, 0
    screen.config(state="normal")
    screen.delete("0.0", END)
    screen.insert("0.0", "This window has no function at the moment...")
    current["text"] = "Current Section: Free Pad"
    screen.config(state="disabled")
    vvv_1.set(free_label)
    del code[:]


def try_a():
    global r, line0, over
    over, r = 0, True
    del code[:]
    if custom_bool:
        line0 = 0
        r = True
        for tag in screen.tag_names():
            screen.tag_delete(tag)
    vvv_1.set('')
    stop_event.set()


root = Tk()
root.title("MorseSim")
root.geometry("800x280")
root.iconbitmap("morse_key.ico")

vvv_1 = StringVar()
screen = Text(root, height=8, width=70)
screen.insert("0.0", "This window has no function at the moment...")
screen.config(state="disabled")
screen_1 = Label(root, textvariable=vvv_1, bg='black', fg='white', height=8, width=80)
screen.place(x=5, y=5)
screen_1.place(x=5, y=150)
vvv_1.set(free_label)

root.focus_set()
Label(root, text="Transmit", font=("arial 14 point", 15)).place(x=580, y=5)

custom_bool = False
Button(root, text="Choose Random text", command=random_text1, width=18).place(x=580, y=40)
Button(root, text="Choose Custom text", command=custom_text1, width=18).place(x=580, y=70)
Button(root, text="Free Pad", command=free_pad1, width=8).place(x=580, y=100)
Button(root, text="Try Again", command=try_a, width=8).place(x=650, y=100)

Label(root, text="Speed (wpm): ").place(x=580, y=140)
var = StringVar()
spin = Spinbox(root, from_=6, to=30, width=5, textvariable=var)
spin.place(x=660, y=142)
var.set(24)

KeyPress = Canvas(root, width=55, height=25, bg="grey55", borderwidth=5, relief="groove", cursor="cross")
KeyPress.place(x=580, y=170)
KeyPress.create_text(34, 18, fill="darkblue", text="KeyPress")
Label(root, text="<< Morse Key").place(x=655, y=176)

Button(root, text="Clear Text", command=free_pad1, width=8).place(x=580, y=210)
current = Label(root, text='Current Section: Free Pad', font=('arial 14 point', 11),
                width=22, borderwidth=7, relief='groove')
current.place(x=580, y=245)

first_control = threading.Thread(target=control, args=(spin, KeyPress, screen_1, vvv_1, screen))
first_control.start()

root.mainloop()

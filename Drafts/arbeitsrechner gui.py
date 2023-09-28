from tkinter import *

window = Tk()
test = 0
button = Button(
    text="Berechnen",
    width=20,
    height=3,
    bg="white",
    fg="red"
)

entry_BG_time = tk.Entry(fg="red", bg="white", width=20)
entry_ED_Time = tk.Entry(fg="red", bg="white", width=20)
entry_BD_Time = tk.Entry(fg="red", bg="white", width=20)

warn_text = tk.Label(
    text="Bitte verwende nur Zahlen!",
    fg="red",
    bg="white",
    width=20,
    height=2
)


BG_Text = tk.Label(
    text="Anfangszeit:",
    fg="black",
    bg="white",
    width=10,
    height=2
)

ED_Text = tk.Label(
    text="Feierabend:",
    fg="black",
    bg="white",
    width=10,
    height=2
)


BD_Text = tk.Label(
    text="Pause:",
    fg="black",
    bg="white",
    width=10,
    height=2
)

Beginn = entry_BG_time.get()
Ende = entry_ED_Time.get()
Pause = entry_BD_Time.get()



warn_text.pack()

BG_Text.pack()
entry_BG_time.pack()

ED_Text.pack()
entry_ED_Time.pack()

BD_Text.pack()
entry_BD_Time.pack()

button.pack()

window.mainloop()

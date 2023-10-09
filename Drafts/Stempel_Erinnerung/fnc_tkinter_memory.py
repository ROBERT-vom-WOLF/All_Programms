import tkinter as tk
def giu(text="Stempeln Robin, Stempeln!"):
    window = tk.Tk()
    text = tk.Label(
        text=text,
        foreground="black",
        background="red",
        width=200,
        height=50
    )
    window.attributes("-topmost", True)
    text.pack()
    window.mainloop()

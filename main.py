from tkinter import *
import Settings
# from Minesweeper import Minesweeper

root = Tk()
root.configure(bg="black")

# width x height
root.geometry(f'{Settings.Width}x{Settings.Height}')
root.title("Minesweeper")
root.resizable(False, False)
top_frame = Frame(
    root, bg="red",
    width=1440,
    height=180
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root, bg="blue",
    width=360,
    height=540
)
left_frame.place(x=0, y=180)

root.mainloop()

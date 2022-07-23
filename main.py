from tkinter import *
from Cell import Cell
import Settings
import Util
# from Minesweeper import Minesweeper

root = Tk()
root.configure(bg="black")

# width x height
root.geometry(f'{Settings.WIDTH}x{Settings.HEIGHT}')
root.title(Settings.GAME_NAME)
root.resizable(False, False)

TFrame = Frame(root, bg="black", width=Util.WidthPercentage(100), height=Util.HeightPercentage(25))
TFrame.place(x=0, y=0)

LFrame = Frame(root, bg="black", width=Util.WidthPercentage(25), height=Util.HeightPercentage(75))
LFrame.place(x=0, y=Util.HeightPercentage(25))

CFrame = Frame(root, bg="white", width=Util.WidthPercentage(75), height=Util.HeightPercentage(75))
CFrame.place(x=Util.WidthPercentage(25), y=Util.HeightPercentage(25))

'''
c1 = Cell()
c1.createCell(CFrame)
c1.Cell.grid(column=0, row=0)

c2 = Cell()
c2.createCell(CFrame)
c2.Cell.grid(column=0, row=1)
'''

for x in range(Settings.GRID_LENGTH):
    for y in range(Settings.GRID_HEIGHT):
        c = Cell()
        c.createCell(CFrame)
        c.Cell.grid(column=x, row=y)

root.mainloop()

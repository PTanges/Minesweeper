from tkinter import *
from Cells import Cell
import Settings
import Util

# Draw Game
root = Tk()
root.configure(bg="black")

root.geometry(f'{Settings.WIDTH}x{Settings.HEIGHT}')
root.title(Settings.GAME_NAME)
root.resizable(False, False)

TFrame = Frame(root, bg="black", width=Util.WidthPercentage(100), height=Util.HeightPercentage(25))
TFrame.place(x=0, y=0)

LFrame = Frame(root, bg="black", width=Util.WidthPercentage(25), height=Util.HeightPercentage(75))
LFrame.place(x=0, y=Util.HeightPercentage(25))
Cell.createCellCountTrackerLabel(LFrame)
Cell.cellCount.place(x=0,y=0)

CFrame = Frame(root, bg="white", width=Util.WidthPercentage(75), height=Util.HeightPercentage(75))
CFrame.place(x=Util.WidthPercentage(25), y=Util.HeightPercentage(25))

for x in range(Settings.GRID_LENGTH):
    for y in range(Settings.GRID_HEIGHT):
        c = Cell(x, y)
        c.createCell(CFrame)
        c.Cell.grid(column=x, row=y)

Cell.randomizeMines()

root.mainloop()

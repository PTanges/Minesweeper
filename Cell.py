from tkinter import Button
import random
import Settings

class Cell:
    # Cache
    map = []
    def __init__(self, x, y, isMine = False):
        self._x = x
        self._y = y
        self._isMine = isMine
        self._CellBox = None

        Cell.map.append(self)

    def createCell(self, location):
        button = Button(location, width = 12, height = 4)
        button.bind('<Button-1>', self.leftClickEvent )
        button.bind('<Button-3>', self.rightClickEvent )
        self._CellBox = button

    def leftClickEvent(self, event):
        pass

    def rightClickEvent(self, event):
        print(event)

    @property
    def isMine(self):
        return self._isMine

    @property
    def Cell(self):
        return self._CellBox

    @staticmethod
    def randomizeMines():
        #map = []
        Settings.MINE_QUANTITY = 5
        mineCellList = random.sample(Cell.map, Settings.MINE_QUANTITY)
        for cellBox in mineCellList:
            cellBox._isMine = True

    # Debug
    def __repr__(self):
        return f'Cell({self._x},{self._y})'
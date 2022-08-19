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
        self._Cell = None

        Cell.map.append(self)

    def createCell(self, location):
        button = Button(location, width=12, height=4)
        button.bind('<Button-1>', self.leftClickEvent)
        button.bind('<Button-3>', self.rightClickEvent)
        self._Cell = button

    def leftClickEvent(self, event):
        if self._isMine:
            self.revealMine()
        else:
            self.revealCell()


    def rightClickEvent(self, event):
        print(event)

    def revealMine(self):
        self.changeCellColour("Red")
        print(f'Boom! You hit a bomb at {self.getCellCoordinates(self._x, self._y)}')

    def revealCell(self):
        self._Cell.configure(text=self.adjacentMineQuantity)
        print(f'Nearby Bombs: {self.adjacentMineQuantity}')

    @property
    def adjacentCells(self):
        adjacentCells = [
            # Adjacent row above
            self.getCellCoordinates(self._x-1, self._y-1),
            self.getCellCoordinates(self._x, self._y-1),
            self.getCellCoordinates(self._x+1, self._y-1),

            # Adjacent west and east
            self.getCellCoordinates(self._x-1, self._y),
            self.getCellCoordinates(self._x+1, self._y),

            # Adjacent row below
            self.getCellCoordinates(self._x-1, self._y+1),
            self.getCellCoordinates(self._x, self._y+1),
            self.getCellCoordinates(self._x+1, self._y+1)
        ]
        adjacentCells = [cell for cell in adjacentCells if cell is not None]
        return adjacentCells

    # No need for the "get" keyword due to @property class decorator, call like a variable name
    @property
    def adjacentMineQuantity(self):
        mineCounter = 0
        for cell in self.adjacentCells:
            if cell.isMine:
                mineCounter += 1
        return mineCounter

    def getCellCoordinates(self, x, y):
        for cell in self.map:
            if cell._x == x and cell._y == y:
                return cell

    def changeCellColour(self, colour):
        self._Cell.configure(bg=colour)

    @property
    def isMine(self):
        return self._isMine

    @property
    def Cell(self):
        return self._Cell

    @staticmethod
    def randomizeMines():
        Settings.MINE_QUANTITY = 5
        mineCellList = random.sample(Cell.map, Settings.MINE_QUANTITY)
        for cellBox in mineCellList:
            cellBox._isMine = True

    # Debug
    def __repr__(self):
        return f'Cell({self._x},{self._y})'
from tkinter import Button, Label
import random
import Settings

class Cell:
    # Cache
    map = []
    cellCount = None
    def __init__(self, x, y, isMine = False):
        self._x = x
        self._y = y
        self._isMine = isMine
        self._Cell = None

        Cell.map.append(self)

    def createCell(self, location):
        button = Button(location, width=12, height=4)
        button.bind('<Button-1>', self.leftClickEvent)
        button.bind('<Button-3>', self.rightClickEvent) # May be configured differently based on mouse specs
        self._Cell = button

    @staticmethod
    def createCellCountTrackerLabel(location):
        label = Label(location,
                      text=f"Cells Left: {Settings.CELL_COUNT}",
                      width=12, height=4,
                      bg="black", fg="white"
        )
        Cell.cellCount = label

    def leftClickEvent(self, event):
        if self._Cell["bg"] == "Orange":
            return
        if self._isMine and self._Cell["bg"] != "Green":
            self.revealMine()
            self.cellCount.configure(fg="Red")
        else:
            if self.adjacentMineQuantity == 0:
                self.revealAdjacentCells()
            else:
                self.revealCell()
        self.updateCellTracker()

    def updateCellTracker(self):
        shownCellCount = 0
        cellLocation = []
        for cell in self.map:
            if cell._Cell["text"] == None or cell._Cell["text"] == "":
                shownCellCount+=1
                cellLocation.append(cell)
        self.cellCount.configure(text=f'Cells left: {shownCellCount}')

        if shownCellCount == Settings.MINE_QUANTITY and self.cellCount["fg"] != "Red":
            self.cellCount.configure(fg="Green")
            for local in cellLocation:
                local._Cell.configure(bg="Green")


    def rightClickEvent(self, event):
        if self._Cell["bg"] == "Orange":
            self.changeCellColour("SystemButtonFace") # Default
        elif self._Cell["bg"] == "SystemButtonFace" and (self._Cell["text"] == None or self._Cell["text"] == ""):
            self.changeCellColour("Orange")


    def revealAdjacentCells(self):
        self.revealCell()
        for cell in self.adjacentCells:
            cell.revealCell()

    def revealMine(self):
        self.changeCellColour("Red")

    def revealCell(self):
        self._Cell.configure(text=self.adjacentMineQuantity)

    @property
    def adjacentMineQuantity(self):
        mineCounter = 0
        for cell in self.adjacentCells:
            if cell.isMine:
                mineCounter += 1
        return mineCounter

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
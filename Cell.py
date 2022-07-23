from tkinter import Button
import Settings
import Util

class Cell:
    def __init__(self, isMine = False):
        self._isMine = isMine
        self._Cell = None

    @property
    def isMine(self):
        return self._isMine

    @property
    def Cell(self):
        return self._Tile

    def createCell(self, location):
        self._Tile = Button(location)
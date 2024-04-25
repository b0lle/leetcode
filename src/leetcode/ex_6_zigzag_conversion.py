import itertools
import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        breite_diagonale: int = numRows - 2
        vertikale_startnummer: int = numRows + breite_diagonale
        anzahl_vertikaler = math.ceil(len(s) / (numRows + breite_diagonale))

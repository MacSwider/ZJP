from __future__ import annotations

import math

from simple_table import SimpleTable


def _check_axis(axis: str) -> None:
    if axis not in ("col", "row"):
        raise ValueError("axis must be 'col' or 'row'")


class Preprocessing:


    __slots__ = ("__data",)

    def __init__(self, table: SimpleTable):
        self.__data = table

    @property
    def data(self) -> SimpleTable:
        return self.__data

    @data.deleter
    def data(self) -> None:
        rows, cols = self.__data.shape
        if rows == 0 or cols == 0:
            self.__data.data = []
            return
        self.__data.data = [[0] * cols for _ in range(rows)]

    def _get_matrix(self) -> list[list]:
        return self.__data.data

    @staticmethod
    def _lp_norm_vector(vec: list[float], p: float) -> float:
        if p == math.inf:
            return max(abs(x) for x in vec) if vec else 0.0
        if p < 1:
            raise ValueError("p must be >= 1 (or math.inf)")
        s = sum(abs(x) ** p for x in vec)
        return s ** (1.0 / p)

    def lp_norm(self, axis: str, p: float) -> list[float]:
        _check_axis(axis)
        m = self._get_matrix()
        rows, cols = self.__data.shape
        if axis == "col":
            norms = []
            for j in range(cols):
                col = [m[i][j] for i in range(rows)]
                norms.append(self._lp_norm_vector(col, p))
            return norms
        norms = []
        for i in range(rows):
            norms.append(self._lp_norm_vector(m[i], p))
        return norms

    def normalize(self, axis: str, p: float = 2) -> None:

        _check_axis(axis)
        m = self._get_matrix()
        rows, cols = self.__data.shape
        if rows == 0 or cols == 0:
            return

        if axis == "col":
            for j in range(cols):
                col = [m[i][j] for i in range(rows)]
                n = self._lp_norm_vector(col, p)
                if n == 0:
                    continue
                for i in range(rows):
                    m[i][j] /= n
        else:
            for i in range(rows):
                n = self._lp_norm_vector(m[i], p)
                if n == 0:
                    continue
                for j in range(cols):
                    m[i][j] /= n

    def min_max_scaling(self, axis: str) -> None:

        _check_axis(axis)
        m = self._get_matrix()
        rows, cols = self.__data.shape
        if rows == 0 or cols == 0:
            return

        if axis == "col":
            for j in range(cols):
                col = [m[i][j] for i in range(rows)]
                lo, hi = min(col), max(col)
                span = hi - lo
                if span == 0:
                    for i in range(rows):
                        m[i][j] = 0.0
                else:
                    for i in range(rows):
                        m[i][j] = (m[i][j] - lo) / span
        else:
            for i in range(rows):
                row = m[i]
                lo, hi = min(row), max(row)
                span = hi - lo
                if span == 0:
                    for j in range(cols):
                        m[i][j] = 0.0
                else:
                    for j in range(cols):
                        m[i][j] = (m[i][j] - lo) / span

    def standardize(self, axis: str) -> None:

        _check_axis(axis)
        m = self._get_matrix()
        rows, cols = self.__data.shape
        if rows == 0 or cols == 0:
            return

        if axis == "col":
            for j in range(cols):
                col = [m[i][j] for i in range(rows)]
                mean = sum(col) / len(col)
                var = sum((x - mean) ** 2 for x in col) / len(col)
                std = math.sqrt(var)
                if std == 0:
                    for i in range(rows):
                        m[i][j] = 0.0
                else:
                    for i in range(rows):
                        m[i][j] = (m[i][j] - mean) / std
        else:
            for i in range(rows):
                row = m[i]
                mean = sum(row) / len(row)
                var = sum((x - mean) ** 2 for x in row) / len(row)
                std = math.sqrt(var)
                if std == 0:
                    for j in range(cols):
                        m[i][j] = 0.0
                else:
                    for j in range(cols):
                        m[i][j] = (m[i][j] - mean) / std

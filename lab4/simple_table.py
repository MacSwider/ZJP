from copy import deepcopy


class SimpleTable:
    """2D table backed by a list of rows (each row is a list)."""

    __slots__ = ("_data",)

    def __init__(self, data=None):
        if data is None:
            self._data = []
        else:
            self._data = deepcopy(data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = deepcopy(value) if value is not None else []

    @data.deleter
    def data(self):
        self._data = []

    @property
    def shape(self):
        rows = len(self._data)
        cols = len(self._data[0]) if rows else 0
        return (rows, cols)

    def _num_cols(self):
        _, c = self.shape
        return c

    def _num_rows(self):
        return len(self._data)

    def add_row(self, row: list) -> None:
        if not self._data:
            self._data.append(list(row))
            return
        if len(row) != self._num_cols():
            raise ValueError("Row lenght does not match number of columns")
        self._data.append(list(row))

    def add_column(self, column: list) -> None:
        if not self._data:
            self._data = [[v] for v in column]
            return
        if len(column) != self._num_rows():
            raise ValueError("Column length does not match number of rows")
        for i, v in enumerate(column):
            self._data[i].append(v)

    def insert_row(self, index: int, row: list) -> None:
        if not self._data:
            if index != 0:
                raise ValueError("Empty table: only row index 0 is allowed")
            self._data.append(list(row))
            return
        if len(row) != self._num_cols():
            raise ValueError("Row length does not match number of columns")
        self._data.insert(index, list(row))

    def insert_column(self, index: int, column: list) -> None:
        if not self._data:
            if index != 0:
                raise ValueError("Empty table: only column index 0 is allowed")
            self._data = [[v] for v in column]
            return
        if len(column) != self._num_rows():
            raise ValueError("Column length does not match number of rows")
        for i, v in enumerate(column):
            self._data[i].insert(index, v)

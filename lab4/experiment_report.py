class ExperimentReport:


    def __init__(self, experiment_name: str, tp=0, fp=0, tn=0, fn=0):
        self.__experiment_name = experiment_name
        self._tp = tp
        self._fp = fp
        self._tn = tn
        self._fn = fn

    @property
    def experiment_name(self) -> str:
        return self.__experiment_name

    @experiment_name.setter
    def experiment_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Experiment name must be a str")
        self.__experiment_name = value

    @experiment_name.deleter
    def experiment_name(self) -> None:
        del self.__experiment_name

    @property
    def tp(self) -> int:
        return self._tp

    @tp.setter
    def tp(self, value: int) -> None:
        if value < 0:
            raise ValueError("Values cannot be negative")
        self._tp = value

    @tp.deleter
    def tp(self) -> None:
        del self._tp

    @property
    def fp(self) -> int:
        return self._fp

    @fp.setter
    def fp(self, value: int) -> None:
        if value < 0:
            raise ValueError("Values cannot be negative")
        self._fp = value

    @fp.deleter
    def fp(self) -> None:
        del self._fp

    @property
    def tn(self) -> int:
        return self._tn

    @tn.setter
    def tn(self, value: int) -> None:
        if value < 0:
            raise ValueError("Values cannot be negative")
        self._tn = value

    @tn.deleter
    def tn(self) -> None:
        del self._tn

    @property
    def fn(self) -> int:
        return self._fn

    @fn.setter
    def fn(self, value: int) -> None:
        if value < 0:
            raise ValueError("Values cannot be negative")
        self._fn = value

    @fn.deleter
    def fn(self) -> None:
        del self._fn

    @property
    def accuracy(self) -> float:
        s = self._tp + self._tn + self._fp + self._fn
        if s == 0:
            return 0.0
        return (self._tp + self._tn) / s

    @property
    def precision(self) -> float:
        d = self._tp + self._fp
        if d == 0:
            return 0.0
        return self._tp / d

    @property
    def recall(self) -> float:
        d = self._tp + self._fn
        if d == 0:
            return 0.0
        return self._tp / d

    @property
    def f1(self) -> float:
        p, r = self.precision, self.recall
        if p + r == 0:
            return 0.0
        return 2 * p * r / (p + r)

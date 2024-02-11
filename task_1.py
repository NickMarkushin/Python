if __name__ == "__main__":
    class Rocket:
        """Класс, описывающий ракету"""

        def __init__(self, name: str, range: float):
            self._name = name
            self._range = range

        def __str__(self):
            return f"Ракета {self._name}. Дальность полета {self._range}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self._name!r}, range={self._range!r})"

        @property
        def name(self) -> str:
            return self._name

        """Возвращает название ракеты"""

        @property
        def range(self) -> float:
            return self._range

        """Возвращает расстояние полета"""


    class ZRK(Rocket):
        def __init__(self, name: str, range: float, max_target_speed: float):
            super().__init__(name=name, range=range)
            self._max_target_speed = max_target_speed

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self._name!r}, range={self._range!r}, max_target_speed={self._max_target_speed})"

        @property
        def range(self) -> float:
            return self._range

        """Возвращает макс. высоту сбития"""
        """Метод перегружен, т.к. в случае ЗРК расстоянием будет являться максимальная высота сбития ЛА"""

        @property
        def max_target_speed(self) -> float:
            return self._max_target_speed

        """Возвращает максимальную скорость цели"""


    pass

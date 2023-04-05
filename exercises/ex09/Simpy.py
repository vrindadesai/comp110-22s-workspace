
"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    def __init__(self, val_list: list):
        """Constructor for Simpy."""
        self.values = val_list
        return

    def __str__(self) -> str:
        """Magic method for str, produces string representation."""    
        return f"Simpy([{self.values}])"

    def fill(self, value: float, times: int) -> None:
        """Fills with repeating value."""
        self.values.clear()
        i: int = 0
        while i < times:
            self.values.append(value)
            i += 1
        return

    def arange(self, start: float, stop: float, step: float = 1) -> None:
        """Fills with values according to step in range."""
        assert step != 0.0
        self.values.clear()
        while start < stop:
            self.values.append(start)
            start += step
        if step < 0:
            while start > stop:
                self.values.append(start)
                start += step
        return

    def sum(self) -> float:
        """sum baby."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """add."""
        new: list = []
        i: int = 0
        if type(rhs) is float:
            for value in self.values:
                new.append(value + rhs)
        else:
            for value in self.values:
                new.append(value + rhs.values[i])
                i += 1
        return Simpy(new)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """pow."""
        new: list = []
        i: int = 0
        if type(rhs) is float:
            for value in self.values:
                new.append(value ** rhs)
        else:
            for value in self.values:
                new.append(value ** rhs.values[i])
                i += 1
        return Simpy(new)

    def __eq__(self, rhs: Union[float, Simpy]) -> list:
        """eq."""
        new: list = []
        i: int = 0
        if type(rhs) is float:
            for value in self.values:
                new.append(value == rhs)
        else:
            for value in self.values:
                new.append(value == rhs.values[i])
                i += 1
        return new

    def __gt__(self, rhs: Union[float, Simpy]) -> list:
        """eq."""
        new: list = []
        i: int = 0
        if type(rhs) is float:
            for value in self.values:
                new.append(value > rhs)
        else:
            for value in self.values:
                new.append(value > rhs.values[i])
                i += 1
        return new

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """g2."""
        new: list = []
        if type(rhs) is int:
            return self.values[rhs]
        else:
            i: int = 0
            for boolean in rhs:
                if boolean:
                    new.append(self.values[i])
                i += 1
        return Simpy(new)

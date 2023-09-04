from abc import abstractmethod
from typing import List
from dataclasses import dataclass

import plotly.graph_objects as go


@dataclass
class EzPlotly:
    rows: int
    cols: int
    secondary: bool

    @abstractmethod
    def add_trace(self): ...

    @abstractmethod
    def format_x_axis(self): ...

    @abstractmethod
    def format_y_axis(self): ...

    @abstractmethod
    def format_layout(self): ...


class EzScatter(EzPlotly):
    def __init__(self, x: List, y: List, rows: int, cols: int, secondary: bool):
        super().__init__(rows, cols, secondary)
        self.x = x
        self.y = y

    def add_trace(self):
        pass


    def format_x_axis(self):
        pass

    def format_y_axis(self):
        pass

    def format_layout(self):
        pass



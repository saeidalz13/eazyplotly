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
    def format_x_axis(self): ...

    @abstractmethod
    def add_trace(self): ...

    @abstractmethod
    def format_y_axis(self): ...


class EzScatter(EzPlotly):
    def __init__(self, rows, cols, secondary):
        super().__init__(rows, cols, secondary)

    def format_x_axis(self):
        pass

    def format_y_axis(self):
        pass

    def add_trace(self):
        pass


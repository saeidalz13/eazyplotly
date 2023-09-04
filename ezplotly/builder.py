from abc import abstractmethod
from typing import Dict, List
from dataclasses import dataclass
from ezplotly.constants import SCATTER_SETTINGS
from plotly.subplots import make_subplots

import plotly.graph_objects as go


@dataclass
class EzPlotly:
    traces: List[List[float | int]]
    rows: int
    cols: int
    secondary: List[bool]

    @property
    @abstractmethod
    def traces_len(self) -> int: ...

    @abstractmethod
    def _create_fig(self) -> None: ...

    @abstractmethod
    def _add_trace(self) -> List[go.Scatter]: ...

    @abstractmethod
    def _format_x_axis(self) -> None: ...

    @abstractmethod
    def _format_y_axis(self) -> None: ...

    @abstractmethod
    def _format_layout(self) -> None: ...


class EzScatter2D(EzPlotly):
    def __init__(
            self, data: List[List[float | int]],
            rows: int, cols: int,
            secondary: List[bool], names: List[str],
            title_text_plot: str = "Plot",
            title_text_xaxis: str = "X",
            title_text_yaxis: str = "Y"
    ) -> None:
        super().__init__(data, rows, cols, secondary)
        self.data = data
        self.names = names
        self.title_text_plot = title_text_plot
        self.title_text_xaxis = title_text_xaxis
        self.title_text_yaxis = title_text_yaxis
        self.fig = None

    @property
    def traces_len(self):
        return len(self.data)

    def _create_fig(self) -> None:
        specs = []
        for n, _ in enumerate(self.secondary):
            spec = [{"secondary_y": self.secondary[n]}]
            specs.append(spec)

        self.fig = make_subplots(
            rows=self.rows,
            cols=self.cols,
            specs=specs
        )

    def _add_trace(self, scatter_settings: Dict = SCATTER_SETTINGS) -> List[go.Scatter]:
        traces = []
        name_idx = 0
        for tn in range(0, self.traces_len, 2):
            trace = go.Scatter(
                x=self.traces[tn],
                y=self.traces[tn + 1],
                mode=scatter_settings["mode"],
                marker=dict(
                    size=scatter_settings["size"],
                    symbol=scatter_settings["symbol"]
                ),
                name=self.names[name_idx]
            )
            traces.append(trace)
            name_idx += 1

        return traces

    def _scatter_2d(self, traces):
        self.fig = go.Figure(traces)

    def _format_x_axis(self, scatter_settings: Dict = SCATTER_SETTINGS) -> None:
        self.fig.update_xaxes(
            title_text=self.title_text_xaxis,
            title_font_size=scatter_settings["title_font_size"],
            title_font_family=scatter_settings["title_font_family"],
            ticks=scatter_settings["ticks"],
            color=scatter_settings["color"],
            gridcolor=scatter_settings["gridcolor"],
            griddash=scatter_settings["griddash"],
            linecolor=scatter_settings["linecolor"],
            linewidth=scatter_settings["linewidth"],
            exponentformat=scatter_settings["exponentformat"]
        )

    def _format_y_axis(self, scatter_settings: Dict = SCATTER_SETTINGS) -> None:
        self.fig.update_yaxes(
            title_text=self.title_text_yaxis,
            title_font_size=scatter_settings["title_font_size"],
            title_font_family=scatter_settings["title_font_family"],
            ticks=scatter_settings["ticks"],
            color=scatter_settings["color"],
            gridcolor=scatter_settings["gridcolor"],
            griddash=scatter_settings["griddash"],
            linecolor=scatter_settings["linecolor"],
            linewidth=scatter_settings["linewidth"],
            exponentformat=scatter_settings["exponentformat"]
        )

    def _format_layout(self, scatter_settings: Dict = SCATTER_SETTINGS) -> None:
        self.fig.update_layout(
            title_text=self.title_text_plot,
            showlegend=scatter_settings["showlegend"],
            plot_bgcolor=scatter_settings["plot_bgcolor"],
            paper_bgcolor=scatter_settings["paper_bgcolor"],
            legend=scatter_settings["legend"]
        )

    def create_plot(self):
        self._create_fig()
        traces = self._add_trace()
        self._scatter_2d(traces)

        self._format_x_axis()
        self._format_y_axis()
        self._format_layout()

        return self.fig


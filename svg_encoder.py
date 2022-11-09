from exception import CustomException
from figures import GeometricFigures


class SVGEncoder:
    def __init__(self,
                 figure_type: str = GeometricFigures.circle.value,
                 figure_size: int = 120,
                 colour: str = "000000"):
        self.figure_type: str = self._get_validated_figure(figure_type)
        self.size = figure_size
        self.colour = "#" + colour

    @staticmethod
    def _get_validated_figure(figure_type: str) -> str:
        figure_type = figure_type.lower().strip()
        available_figures = GeometricFigures.get_all_values()

        if figure_type not in available_figures:
            message = f"Figure '{figure_type}' is not available. Available figures: {str(available_figures)[1:-1]}"
            raise CustomException(message)

        return figure_type

    def get_svg_code(self) -> str:
        match self.figure_type:
            case GeometricFigures.square.value | GeometricFigures.rectangle.value:
                return self._get_rectangle()
            case GeometricFigures.circle.value | GeometricFigures.ellipse.value:
                return self._get_ellipse()
            case _:
                message = f"Not founded logic for {self.figure_type}"
                raise CustomException(message)

    @staticmethod
    def _get_head(width: int, height: int):
        return f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'

    def _get_ellipse(self) -> str:
        is_circle = self.figure_type == GeometricFigures.circle.value
        x_size = self.size if is_circle else self.size // 2
        y_size = self.size

        head = self._get_head(width=x_size * 2, height=y_size * 2)

        body = f'<ellipse fill="{self.colour}" cx="{x_size}" rx="{x_size}" cy="{y_size}" ry="{y_size}"/>'

        return f"{head}\n  {body}\n</svg>"

    def _get_rectangle(self) -> str:
        is_square = self.figure_type == GeometricFigures.square.value
        x_size = self.size if is_square else self.size // 2
        y_size = self.size

        head = self._get_head(width=x_size, height=y_size)

        body = f'<rect fill="{self.colour}" width="{x_size}" height="{y_size}"/>'

        return f"{head}\n  {body}\n</svg>"

from enum import Enum
from typing import List


class GeometricFigures(Enum):
    circle = "circle"
    square = "square"
    rectangle = "rectangle"
    ellipse = "ellipse"

    @classmethod
    def get_all_values(cls) -> List:
        return [figure.value for figure in cls]

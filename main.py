import sys

from svg_encoder import SVGEncoder
from figures import GeometricFigures
from exception import CustomException


def create_svg(code: str, path: str = None) -> None:
    path = path or "result.svg"
    with open(path, "w") as file:
        file.write(code)


if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        figure_type = args[0] if args else GeometricFigures.circle
        figure_size = int(args[1]) if len(args) >= 2 else 120
        colour = args[2] if len(args) >= 3 else "000000"

        encoder = SVGEncoder(figure_type, figure_size, colour)
        svg_code = encoder.get_svg_code()

        save_to = args[3] if len(args) >= 4 else "result.svg"
        create_svg(svg_code, save_to)
    except CustomException as err:
        print(err.message)

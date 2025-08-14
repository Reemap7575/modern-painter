from dataclasses import dataclass

@dataclass
class PaintCalculator:
    width: float
    height: float
    copies: int
    paint_color: str = "undefined"

    def triangle_height(self) -> float:
        # Triangle base = width / 3, height equals rectangle's height
        return self.height

    def single_copy_area(self) -> float:
        rectangle_area = self.width * self.height
        triangle_base = self.width / 3
        triangle_height = self.triangle_height()
        triangle_area = (triangle_base * triangle_height) / 2
        return rectangle_area + triangle_area

    def total_paint_area(self) -> float:
        return self.single_copy_area() * self.copies

    def set_paint_color(self, color: str):
        self.paint_color = color

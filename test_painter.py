import pytest
from src.painter import PaintCalculator

def test_triangle_height_matches_rectangle_height():
    pc = PaintCalculator(width=9.0, height=4.0, copies=1)
    assert pc.triangle_height() == pytest.approx(4.0)

def test_single_copy_area_computation():
    # width=3, height=2 → rectangle=6, triangle base=1, triangle area=1
    pc = PaintCalculator(width=3.0, height=2.0, copies=1)
    assert pc.single_copy_area() == pytest.approx(7.0)

def test_total_paint_area_multiple_copies():
    pc = PaintCalculator(width=3.0, height=2.0, copies=5000)
    assert pc.total_paint_area() == pytest.approx(7.0 * 5000)

def test_set_paint_color_assigns_properly():
    pc = PaintCalculator(width=1.0, height=1.0, copies=1)
    pc.set_paint_color("blue")
    assert pc.paint_color == "blue"

# type: ignore
import pytest
from pytest import approx

from figure_tools import apply_style, create_figure, validate_size

_default_width = 3.15
_default_height = 2.36


def test_validate_size():
    assert validate_size(1.5) == 1.5
    assert validate_size(1.5, size='default') == 1.5
    assert validate_size(1.5, size='2x') == 3.0
    assert validate_size(1.5, size='80mm') == 80 / 25.4
    assert validate_size(1.5, size='6cm') == 6 / 2.54
    assert validate_size(1.5, size='4inch') == 4
    assert validate_size(2.0, size='0.25x') == 0.5
    assert validate_size(2.0, size='0.2x') == 0.4
    pytest.raises(ValueError, lambda: validate_size('x'))
    pytest.raises(ValueError, lambda: validate_size(1, size='1,5mm'))
    pytest.raises(ValueError, lambda: validate_size(1, size='1.mm'))
    pytest.raises(ValueError, lambda: validate_size(1, size='1..5mm'))
    pytest.raises(ValueError, lambda: validate_size(1, size='1.5miles'))


def test_default_figure_size():
    apply_style()
    fig = create_figure()
    assert fig.get_figwidth() == _default_width
    assert fig.get_figheight() == _default_height


def test_absolute_figure_size():
    apply_style()
    fig = create_figure(width=11, height=7)
    assert fig.get_figwidth() == approx(11, 0.01)
    assert fig.get_figheight() == approx(7, 0.01)


def test_scaled_figure_size():
    apply_style()
    fig = create_figure(width='2x', height='1.5x')
    assert fig.get_figwidth() == approx(2 * _default_width, 0.01)
    assert fig.get_figheight() == approx(1.5 * _default_height, 0.01)


def test_scaled_figure_size2():
    apply_style()
    fig = create_figure(width='2x', height='0.25x')
    assert fig.get_figwidth() == approx(2 * _default_width, 0.01)
    assert fig.get_figheight() == approx(0.25 * _default_height, 0.01)


def test_figure_size_with_units():
    apply_style()
    fig = create_figure(width='80mm', height='6cm')
    assert fig.get_figwidth() == approx(80 / 25.4, 0.01)
    assert fig.get_figheight() == approx(6 / 2.54, 0.01)


def test_aspect_ratio_with_default_width():
    apply_style()
    fig = create_figure(aspect_ratio=2.0)
    assert fig.get_figwidth() == approx(_default_width, 0.01)
    assert fig.get_figheight() == approx(2 * _default_width, 0.01)


def test_aspect_ratio_with_absolute_width():
    apply_style()
    fig = create_figure(width='120mm', aspect_ratio=0.5)
    assert fig.get_figwidth() == approx(120 / 25.4, 0.01)
    assert fig.get_figheight() == approx(0.5 * 120 / 25.4, 0.01)

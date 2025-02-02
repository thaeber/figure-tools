import os
import re as regex
from typing import Union, Tuple, Dict, Any, Optional
import warnings

import matplotlib.colors
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def apply_style(*additional_styles):
    """
    Applies a commong style to all figures created after calling this function.
    """
    plt.style.use(os.path.join(os.path.dirname(__file__), './figure_style.mplstyle'))

    for style in additional_styles:
        plt.style.use(style)


def _validate_float(s: Union[str, float]) -> float:
    """convert s to float or raise"""
    try:
        return float(s)
    except ValueError:
        raise ValueError('Could not convert "%s" to float' % s)


def validate_size(default_size: float, size: Union[float, str] = 'default') -> float:
    """Validates and returns the figure size.

    ### Args:

    - `default_size` (float): The default size in inch.
    - `size` (float, str), optional: A float specifying the absolute size in inch
        or a string value representing the size or size modifier.
        String values can be of the following form:
        'default': The default size.
        '1.5x': A multiplier (here 1.5) of the default size.
        '80mm': The absolute size in millimeter (here 80mm).
        '6cm': The aboslute size in centimeter (here 6cm).
        '3inch': The absolute size in inch (here 3inch).

    ### Raises:

        `ValueError`: The parameter 'size' is not a valid size specification.

    ### Returns:
        `float`: The final absolute size in inch.
    """
    default_size = _validate_float(default_size)
    if isinstance(size, str):
        if size == 'default':
            return default_size
        else:
            pattern = r"^(\d+(?:\.\d+)?|\d*(?:\.\d+))\s*(x|mm|cm|inch)$"
            match = regex.match(pattern, size)
            if match is not None:
                value = _validate_float(match.group(1))
                unit = match.group(2)
                if unit == 'x':
                    return default_size * value
                elif unit == 'mm':
                    return value / 25.4
                elif unit == 'cm':
                    return value / 2.54
                elif unit == 'inch':
                    return value
                else:
                    raise ValueError(f'Unrecognized unit "{unit}" in "{size}".')
            else:
                raise ValueError(
                    f'"{size}" is not a valid figure size specification. '
                    'Valid values are, e.g. "8cm", "80mm", "3inch" or "2x."'
                )
    else:
        return _validate_float(size)


def create_figure(
    width: Union[float, str] = 'default',
    height: Union[float, str] = 'default',
    aspect_ratio: Optional[float] = None,
    **fig_kws: Dict[str, Any],
) -> Figure:
    """
    Creates a new figure with given size and/or aspect ratio

    ### Args:

    - `width` (float or string):
        Specifies the width of the figure. Defaults to 'default'. Possible values are:
        - `float`: The absolute width in inches.
        - `'default'`: Takes the default width from the rcParams.
        - `'[value][unit]'`: A combination of a floating value and unit.
            Possible units are 'mm', 'cm' and 'inch'. Additionally the
            width can be specified as a multiple of the default width,
            e.g. '2x' or '1.5x'.

    - `height` (float or string):
        Specifies the height of the figure. Defaults to 'default'.
        See the 'width' parameter for possible values.

    - `aspect_ratio` (float or None): If not None, specifies the aspect ratio
        (height/width) of the figure. The parameter is ignored if height is
        not 'default'. Defaults to None.

    ### Returns:

    `Figure`: A reference to the figure instance.

    ### Examples:

        # create a figure with default width and height
        fig = create_figure()

        # create a figure with 1.5-times the default width
        fig = create_figure(width='1.5x')

        # create a figure with absolute width and height in different units
        fig = create_figure(width='80mm', height='6cm')

        # create a figure with a given aspect ratio
        fig = create_figure(aspect_ratio=1.0)
        fig = create_figure(width='50mm', aspect_ratio=0.5)

    """

    # get default width and height from rcParams
    default_sizes: Tuple[float, float] = matplotlib.rcParams['figure.figsize']
    default_width, default_height = default_sizes

    # calculate actual figure width
    actual_width = validate_size(default_width, width)

    # calculate actual figure height
    if (aspect_ratio is not None) and (height == 'default'):
        # aspect ratio is only used if the default height is still set
        actual_height = actual_width * _validate_float(aspect_ratio)
    else:
        if aspect_ratio is not None:
            warnings.warn(
                'Aspect ratio is ignored because a non-default figure'
                ' height was specified.'
            )
        actual_height = validate_size(default_height, height)

    fig = plt.figure(figsize=(actual_width, actual_height), **fig_kws)

    return fig

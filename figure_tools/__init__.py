import os
from typing import Union
from pathlib import Path
from collections import OrderedDict

import matplotlib.pyplot as plt
import matplotlib.colors

# Add light colors from the Tableau 20 colormap to the list of
# named colors in matplotlib. After that, the light colors
# can be used similarly to the "normal" tableau colors when
# plotting.
#
# For example: plt.plot(x, y, color='tab:lightblue')
#
LIGHT_TABLEAU_COLORS = (
    ('blue', '#aec7e8'),
    ('orange', '#ffbb78'),
    ('green', '#98df8a'),
    ('red', '#ff9896'),
    ('purple', '#c5b0d5'),
    ('brown', '#c49c94'),
    ('pink', '#f7b6d2'),
    ('gray', '#c7c7c7'),
    ('olive', '#dbdb8d'),
    ('cyan', '#9edae5'),
)

# Normalize name to "tab:<name>" to avoid name collisions.
LIGHT_TABLEAU_COLORS = OrderedDict(
    ('tab:light' + name, value) for name, value in LIGHT_TABLEAU_COLORS)

# add light tablue colors to the list o named matplotlib colors
matplotlib.colors._colors_full_map.update(LIGHT_TABLEAU_COLORS)


def apply_style():
    plt.style.use(
        os.path.join(os.path.dirname(__file__), './figure_style.mplstyle'))


def create_figure(width=8.0,
                  height=None,
                  aspect_ratio='auto',
                  size_class=1.0,
                  **fig_kws):

    target_width = size_class * width

    if height is None:
        if (aspect_ratio == 'auto') or (aspect_ratio is None):
            target_height = 0.75 * width
        else:
            target_height = aspect_ratio * target_width
    else:
        target_height = size_class * height

    # convert to inch
    target_width /= 2.54
    target_height /= 2.54

    fig = plt.figure(figsize=(target_width, target_height), **fig_kws)

    return fig


def save_figure(filename: str, figure=None, formats=('.png', ), **kws):

    # get default figure
    if figure is None:
        figure = plt.gcf()

    # target filename
    filename = Path(filename)

    # create target path
    filename.parent.mkdir(parents=True, exist_ok=True)

    # merge parameters
    kws = {**dict(dpi=600, transparent=False), **kws}

    # save figure
    for fmt in formats:
        if not fmt.startswith('.'):
            fmt = '.' + fmt
        target = filename.with_suffix(fmt)

        print(f'Saving: {target}')
        print(kws)
        figure.savefig(target, **kws)


def image_path(
    script_path: Union[str, Path],
    images_root_path='images',
    script_root_path=None,
):
    script_path = Path(script_path)
    images_root_path = Path(images_root_path)

    # use parent path if script path contains actual filename
    # if script_path.suffix:
    #     script_path = script_path.parent

    if not script_root_path:
        script_root_path = Path.cwd()

    result = images_root_path / Path(script_path).relative_to(script_root_path)
    return result.with_suffix('.png')

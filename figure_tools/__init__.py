# set package version
__version__ = '0.1.2'

from typing import Union
from pathlib import Path

import matplotlib.pyplot as plt

from . import colors  # type: ignore
from .figure import apply_style, create_figure, validate_size  # type: ignore


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

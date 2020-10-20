import os
from pathlib import Path
from typing import Iterable, Union

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from . import _config


def save_figure(filename: Union[str, Path],
                figure: Union[Figure, None] = None,
                formats: Iterable[str] = ('.png', ),
                **kws):

    # get default figure
    if figure is None:
        figure = plt.gcf()

    # target filename
    filename = build_image_path(filename)

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


def build_image_path(filename: Union[str, Path]) -> Path:

    # make sure filename is of typ Path
    filename = Path(filename)

    # check if a workspace root path is specified
    workspace_root = _config.get_workspace_root()

    # check if an image path is specified
    image_path = _config.get_image_path()

    # build return path
    if image_path is None:
        return filename
    else:
        if workspace_root is None:
            return image_path / filename.name
        else:
            return image_path / filename.resolve().relative_to(
                workspace_root.resolve())

import os
import subprocess
from pathlib import Path
from typing import Iterable, Union
import warnings

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.colors

from . import _config as cfg


def save_figure(filename: Union[str, Path],
                figure: Union[Figure, None] = None,
                formats: Iterable[str] = ('.png', ),
                **kws):

    # make sure filename is of type Path
    filename = Path(filename)

    # if figure is None, get default figure
    if figure is None:
        figure = plt.gcf()

    # add git commit hash as annotation
    if not cfg.do_not_add_commit_hash_annotation:
        # get commit hash
        text = _get_commit_hash()
        if text is None:
            warnings.warn('Could not obtain commit hash.')
        else:
            _add_commit_hash_annotation(text)

    # add filename annotation
    if not cfg.do_not_add_filename_annotation:
        _add_filename_annotation(filename)

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
    workspace_root = cfg.get_workspace_root()

    # check if an image path is specified
    image_path = cfg.get_image_path()

    # build return path
    if image_path is None:
        return filename
    else:
        if workspace_root is None:
            return image_path / filename.name
        else:
            return image_path / filename.resolve().relative_to(
                workspace_root.resolve())


def _add_commit_hash_annotation(text: str):
    _add_annotation(f'git:{text}', loc='upper left')


def _add_filename_annotation(filename: Path):
    _add_annotation(filename.name, loc='upper right')


def _add_annotation(text: str, loc: str):
    kws = dict(
        xycoords='figure fraction',
        textcoords='offset points',
        fontsize=0.6 * matplotlib.rcParams['font.size'],
        # color=matplotlib.colors.to_rgba(figure.get_edgecolor(), 0.5),
        color=matplotlib.colors.to_rgba('black', 0.5),
        annotation_clip=False)

    # default position
    if loc == 'upper left':
        xy = (0.0, 1.0)
        kws.update(ha='left', va='top', xytext=(2, -2))
    elif loc == 'upper right':
        xy = (1.0, 1.0)
        kws.update(
            ha='right',
            va='top',
            xytext=(-2, -2),
        )
    else:
        raise ValueError('"loc" must be one of "upper left" or "upper right"')

    # create annotation
    plt.annotate(text, xy, **kws)


def _get_commit_hash() -> Union[str, None]:
    try:
        label = subprocess.check_output(
            ["git", "describe", "--always", "--dirty"], text=True).strip()
        return str(label)
    except:
        return None
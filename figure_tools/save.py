import os
import datetime
import subprocess
import warnings
from pathlib import Path
from typing import Dict, Iterable, Union
from operator import itemgetter

import matplotlib
import matplotlib.colors
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PIL import Image

from . import _config as cfg


def save_figure(filename: Union[str, Path],
                figure: Union[Figure, None] = None,
                formats: Iterable[str] = ('.png', ),
                index: str = None,
                **kws):

    # make sure filename is of type Path
    filename = Path(filename)

    # if figure is None, get default figure
    if figure is None:
        figure = plt.gcf()

    # add git commit hash to figure metadata
    git_commit = _get_git_commit_hash()
    metadata = kws.setdefault('metadata', {})
    metadata.update({
        'created': f'{datetime.datetime.now(datetime.timezone.utc)}',
        'git-commit': f'{git_commit}',
        'script-filename': filename.name,
        'git-blame': f'{_get_git_blame(filename)}',
    })

    # add git commit hash as annotation
    if not cfg.do_not_add_commit_hash_annotation:
        # get commit hash
        if git_commit is None:
            warnings.warn('Could not obtain commit hash.')
        else:
            _add_commit_hash_annotation(figure, git_commit)

    # add filename annotation
    if not cfg.do_not_add_filename_annotation:
        _add_filename_annotation(figure, filename)

    # target filename
    filename = build_image_path(filename)

    # create target path
    filename.parent.mkdir(parents=True, exist_ok=True)

    # add default keyword arguments
    kws.setdefault('dpi', 600)
    kws.setdefault('transparent', False)

    # save figure
    for fmt in formats:
        if not fmt.startswith('.'):
            fmt = '.' + fmt
        if index is not None:
            if not index.startswith('.'):
                index = '.' + index
            fmt = index + fmt
        target = filename.with_suffix(fmt)

        print(f'Saving: {target}')
        # print(kws)
        figure.savefig(target, **kws)


def load_image_metadata(filename: Union[str, Path]) -> Dict[str, str]:

    filename = Path(filename)

    if filename.suffix == '.py':
        filename = filename.with_suffix('.png')

    img = Image.open(filename.resolve())
    return img.info


def print_image_metadata(filename):
    info = load_image_metadata(filename)
    fmt = '{0:>16} {1}'
    for key in info.keys():
        if key in ['created', 'git-commit', 'script-filename']:
            print(fmt.format(key + ':', info[key]))
        elif key == 'git-blame':
            lines = info['git-blame'].splitlines()
            if len(lines) > 0:
                print(fmt.format(key + ':', lines[0]))
            if len(lines) > 1:
                for line in lines:
                    print(fmt.format('', line))
        else:
            print(fmt.format(key + ':', info[key]))


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


def _add_commit_hash_annotation(figure: Figure, text: str):
    _add_annotation(figure, f'git:{text}', loc='upper left')


def _add_filename_annotation(figure: Figure, filename: Path):
    workspace_root = cfg.get_workspace_root()
    if workspace_root:
        s = str(filename.relative_to(workspace_root))
    else:
        s = filename.name
    _add_annotation(figure, s, loc='upper right')


def _add_annotation(figure: Figure, text: str, loc: str):

    # get axes
    if len(figure.axes) == 1:
        ax = figure.axes[0]
    else:
        if loc == 'upper left':
            # get upper left axis
            axes = [(a, a.get_position().xmin, a.get_position().ymax)
                    for a in figure.axes]
            axes = sorted(axes, key=itemgetter(2),
                          reverse=True)  # sort by ymax
            axes = sorted(axes, key=itemgetter(1))  # sort by xmin
            ax = axes[0][0]
        elif loc == 'upper right':
            # get upper right axis
            axes = [(a, a.get_position().xmax, a.get_position().ymax)
                    for a in figure.axes]
            axes = sorted(axes, key=itemgetter(2),
                          reverse=True)  # sort by ymax
            axes = sorted(axes, key=itemgetter(1),
                          reverse=True)  # sort by xmax
            ax = axes[0][0]
        else:
            raise ValueError(
                '"loc" must be one of "upper left" or "upper right"')

    kws = dict(xycoords='axes fraction',
               textcoords='offset points',
               fontsize=0.6 * matplotlib.rcParams['font.size'],
               color=matplotlib.colors.to_rgba('black', 0.5),
               annotation_clip=False)

    # position
    if loc == 'upper left':
        xy = (0.0, 1.0)
        kws.update(ha='left', va='bottom', xytext=(1, 1))
    elif loc == 'upper right':
        xy = (1.0, 1.0)
        kws.update(
            ha='right',
            va='bottom',
            xytext=(-1, 1),
        )
    else:
        raise ValueError('"loc" must be one of "upper left" or "upper right"')

    # create annotation
    ax.annotate(text, xy, **kws)


def _get_git_commit_hash() -> Union[str, None]:
    try:
        label = subprocess.check_output(
            ["git", "describe", "--always", "--dirty"], text=True).strip()
        return str(label)
    except:
        return None


def _get_git_blame(filename: Path):
    try:
        label = subprocess.check_output(
            ["git", "blame", "-M",
             str(filename.resolve())], text=True)
        return str(label)
    except:
        return None

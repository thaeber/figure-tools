from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pytest

import figure_tools.save as fts
from figure_tools import create_figure, load_image_metadata, save_figure


@pytest.mark.skip(
    reason='spurious failures ::: _tkinter.TclError: invalid command name "tcl_findLibrary"'
)
def test_save_current_figure(tmp_path: Path, monkeypatch):
    # create test figure
    create_figure(width='8cm', aspect_ratio=1)
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.title('test plot')

    # setup environment variables
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', '')
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', '')

    filename = tmp_path / 'a/b/test.py'
    save_figure(filename)  # by default png-files are created

    # make sure the file exists
    assert filename.with_suffix('.png').exists()


@pytest.mark.skip(
    reason='spurious failures ::: _tkinter.TclError: invalid command name "tcl_findLibrary"'
)
def test_save_figure_with_image_path(tmp_path: Path, monkeypatch):
    # create test figure
    create_figure(width='8cm', aspect_ratio=1)
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.title('test plot')

    # setup environment variables
    image_path = tmp_path / 'images'
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', '')
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', str(image_path))

    filename = tmp_path / 'a/b/test.py'
    save_figure(filename)  # by default png-files are created

    # make sure the file exists
    assert (image_path / filename.name).with_suffix('.png').exists()


@pytest.mark.skip(
    reason='spurious failures ::: _tkinter.TclError: invalid command name "tcl_findLibrary"'
)
def test_save_figure_with_image_path_and_workspace(tmp_path: Path, monkeypatch):
    # create test figure
    create_figure(width='8cm', aspect_ratio=1)
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.title('test plot')

    # setup environment variables
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', str(tmp_path / 'images'))
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', str(tmp_path / 'a/b'))

    filename = tmp_path / 'a/b/c/d/test.py'
    save_figure(filename)  # by default png-files are created

    # make sure the file exists
    assert (tmp_path / 'images/c/d' / filename.name).with_suffix('.png').exists()


@pytest.mark.skip(
    reason='spurious failures ::: _tkinter.TclError: invalid command name "tcl_findLibrary"'
)
def test_add_commit_metadata(tmp_path: Path, monkeypatch):
    # create test figure
    create_figure(width='8cm', aspect_ratio=1)
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.title('test plot')
    plt.tight_layout()

    # setup environment variables
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', '')
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', '')

    # save figure
    filename = tmp_path / Path(__file__).name
    save_figure(filename)

    # load image metdata and compare
    info = load_image_metadata(filename.with_suffix('.png'))
    assert info['script-filename'] == filename.name
    assert info['git-commit'] == fts._get_git_commit_hash()

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pytest
from figure_tools import create_figure, save_figure


def test_save_current_figure(tmp_path: Path):
    # create test figure
    fig = create_figure(width='8cm', aspect_ratio=1)
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.title('test plot')

    filename = tmp_path / 'a/b/test.py'
    save_figure(filename)  # by default png-files are created

    # make sure the file exists
    assert filename.with_suffix('.png').exists()


def test_save_figure_with_image_path(tmp_path: Path, monkeypatch):
    # create test figure
    fig = create_figure(width='8cm', aspect_ratio=1)
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.title('test plot')

    # setup environment variables
    image_path = tmp_path / 'images'
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', str(image_path))

    filename = tmp_path / 'a/b/test.py'
    save_figure(filename)  # by default png-files are created

    # make sure the file exists
    assert (image_path / filename.name).with_suffix('.png').exists()


def test_save_figure_with_image_path_and_workspace(tmp_path: Path,
                                                   monkeypatch):
    # create test figure
    fig = create_figure(width='8cm', aspect_ratio=1)
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.title('test plot')

    # setup environment variables
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', str(tmp_path / 'images'))
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', str(tmp_path / 'a/b'))

    filename = tmp_path / 'a/b/c/d/test.py'
    save_figure(filename)  # by default png-files are created

    # make sure the file exists
    assert (tmp_path / 'images/c/d' /
            filename.name).with_suffix('.png').exists()


def test_add_commit_hash_as_annotation():

    # create test figure
    fig = create_figure(width='8cm', aspect_ratio=1)
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.title('test plot')
    plt.tight_layout()

    # save figure
    save_figure('baseline/test.py')

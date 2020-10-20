import os
from pathlib import Path
from figure_tools import image_path

import pytest


def test_unmodified_path():
    assert image_path('test/hallo.py') == Path('test/hallo.py')


def test_env_image_path_wo_workspace(monkeypatch):
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', 'a/images')
    assert image_path('a/b/c/d/test.py') == Path('a/images/test.py')


def test_env_image_path_with_workspace(monkeypatch):
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', 'a/images')
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', 'a/b')
    assert image_path('a/b/c/d/test.py') == Path('a/images/c/d/test.py')


def test_env_workspace_wo_image_path(monkeypatch):
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', 'a/b')
    assert image_path('a/b/c/d/test.py') == Path('a/b/c/d/test.py')
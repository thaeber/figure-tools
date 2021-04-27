import os
from pathlib import Path
from figure_tools.save import build_image_path

import pytest


def test_unmodified_path(monkeypatch):
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', '')
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', '')
    assert build_image_path('test/hallo.py') == Path('test/hallo.py')


def test_env_image_path_wo_workspace(monkeypatch):
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', '')
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', 'a/images')
    assert build_image_path('a/b/c/d/test.py') == Path('a/images/test.py')


def test_env_image_path_with_workspace(monkeypatch):
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', 'a/images')
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', 'a/b')
    assert build_image_path('a/b/c/d/test.py') == Path('a/images/c/d/test.py')


def test_env_workspace_wo_image_path(monkeypatch):
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', 'a/b')
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', '')
    assert build_image_path('a/b/c/d/test.py') == Path('a/b/c/d/test.py')
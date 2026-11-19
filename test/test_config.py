from pathlib import Path

from figure_tools._config import get_git_root, get_image_path, get_workspace_root


def test_default_image_path():
    # by default, the image path is below the git root directory
    assert get_image_path() == Path('images')
    # assert get_image_path() == Path(__file__).parent.parent / 'images'


def test_custom_image_path(monkeypatch):
    monkeypatch.setenv('FIG_TOOLS_IMAGE_PATH', 'temp/myimages')
    assert get_image_path() == Path('temp/myimages')


def test_git_root_dir():
    assert get_git_root() == Path(__file__).parent.parent


def test_default_workspace_root():
    assert get_workspace_root() == get_git_root()


def test_custom_workspace_root(monkeypatch):
    monkeypatch.setenv('FIG_TOOLS_WORKSPACE_ROOT', 'myroot')
    assert get_workspace_root() == Path('myroot')

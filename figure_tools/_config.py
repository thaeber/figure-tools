import os
from pathlib import Path
import subprocess
from typing import Union

do_not_add_commit_hash_annotation = False
do_not_add_filename_annotation = False


def get_image_path() -> Union[Path, None]:
    # check for environment variable
    path = os.getenv('FIG_TOOLS_IMAGE_PATH')
    if path == '':
        return None
    elif path is not None:
        return Path(path)
    else:
        return Path('images')


def get_git_root() -> Union[Path, None]:
    try:
        label = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True).strip()
        return Path(label)
    except:
        return None


def get_workspace_root() -> Union[Path, None]:
    # check for environment variable
    env_path = os.getenv('FIG_TOOLS_WORKSPACE_ROOT')
    if env_path == '':
        return None
    elif env_path is not None:
        return Path(env_path)

    # check for root folder of git repository
    git_path = get_git_root()
    if git_path is not None:
        return git_path

    return None

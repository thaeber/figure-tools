import os
from pathlib import Path
from typing import Union

do_not_add_commit_hash_annotation = False
do_not_add_filename_annotation = False


def get_image_path() -> Union[Path, None]:
    # check for environment variable
    path = os.getenv('FIG_TOOLS_IMAGE_PATH')
    if path is not None:
        return Path(path)
    else:
        return path


def get_workspace_root() -> Union[Path, None]:
    # check for environment variable
    path = os.getenv('FIG_TOOLS_WORKSPACE_ROOT')
    if path is not None:
        return Path(path)
    else:
        return path

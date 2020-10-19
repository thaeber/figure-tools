import os
from pathlib import Path
from typing import Union


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

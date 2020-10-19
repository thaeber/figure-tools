# set package version
__version__ = '0.1.3'

from typing import Union
from pathlib import Path

import matplotlib.pyplot as plt

from . import colors  # type: ignore
from .figure import apply_style, create_figure, validate_size  # type: ignore
from .save import save_figure, image_path

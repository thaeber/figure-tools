# Add light colors from the Tableau 20 colormap to the list of
# named colors in matplotlib. After that, the light colors
# can be used similarly to the "normal" tableau colors when
# plotting.
#
# For example: plt.plot(x, y, color='tab:lightblue')
#
from typing import OrderedDict
import matplotlib.colors

LIGHT_TABLEAU_COLORS = (
    ('blue', '#aec7e8'),
    ('orange', '#ffbb78'),
    ('green', '#98df8a'),
    ('red', '#ff9896'),
    ('purple', '#c5b0d5'),
    ('brown', '#c49c94'),
    ('pink', '#f7b6d2'),
    ('gray', '#c7c7c7'),
    ('olive', '#dbdb8d'),
    ('cyan', '#9edae5'),
)

# Normalize name to "tab:<name>" to avoid name collisions.
LIGHT_TABLEAU_COLORS = OrderedDict(
    ('tab:light' + name, value) for name, value in LIGHT_TABLEAU_COLORS)

# add light tablue colors to the list o named matplotlib colors
matplotlib.colors._colors_full_map.update(LIGHT_TABLEAU_COLORS)
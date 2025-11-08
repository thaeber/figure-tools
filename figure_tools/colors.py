# Add light colors from the Tableau 20 colormap to the list of
# named colors in matplotlib. After that, the light colors
# can be used similarly to the "normal" tableau colors when
# plotting.
#
# For example: plt.plot(x, y, color='tab:lightblue')
#
from collections import OrderedDict
import matplotlib.colors
from matplotlib.colors import to_rgb

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
    ('tab:light' + name, value) for name, value in LIGHT_TABLEAU_COLORS
)

# add light tableau colors to the list o named matplotlib colors
matplotlib.colors._colors_full_map.update(LIGHT_TABLEAU_COLORS)

# Extended tableau colors
EXTENDED_TABLEAU_COLORS = (
    ('black', '#000000'),
    ('light', '#c7c7c7'),
)
EXTENDED_TABLEAU_COLORS = OrderedDict(
    ('tab:' + name, value) for name, value in EXTENDED_TABLEAU_COLORS
)
matplotlib.colors._colors_full_map.update(EXTENDED_TABLEAU_COLORS)

# add tab20 color shades
TAB20_SHADED_COLORS = (
    ('indigo1', '#393b79'),
    ('indigo2', '#5254a3'),
    ('indigo3', '#6b6ecf'),
    ('indigo4', '#9c9ede'),
    ('olive1', '#637939'),
    ('olive2', '#8ca252'),
    ('olive3', '#b5cf6b'),
    ('olive4', '#cedb9c'),
    ('brown1', '#8c6d31'),
    ('brown2', '#bd9e39'),
    ('brown3', '#e7ba52'),
    ('brown4', '#e7cb94'),
    ('firebrick1', '#843c39'),
    ('firebrick2', '#ad494a'),
    ('firebrick3', '#d6616b'),
    ('firebrick4', '#e7969c'),
    ('purple1', '#7b4173'),
    ('purple2', '#a55194'),
    ('purple3', '#ce6dbd'),
    ('purple4', '#de9ed6'),
    ('blue1', '#3182bd'),
    ('blue2', '#6baed6'),
    ('blue3', '#9ecae1'),
    ('blue4', '#c6dbef'),
    ('orange1', '#e6550d'),
    ('orange2', '#fd8d3c'),
    ('orange3', '#fdae6b'),
    ('orange4', '#fdd0a2'),
    ('green1', '#31a354'),
    ('green2', '#74c476'),
    ('green3', '#a1d99b'),
    ('green4', '#c7e9c0'),
    ('mediumpurple1', '#756bb1'),
    ('mediumpurple2', '#9e9ac8'),
    ('mediumpurple3', '#bcbddc'),
    ('mediumpurple4', '#dadaeb'),
    ('gray1', '#636363'),
    ('gray2', '#969696'),
    ('gray3', '#bdbdbd'),
    ('gray4', '#d9d9d9'),
)

# Normalize name to "tab:<name>" to avoid name collisions.
TAB20_SHADED_COLORS = OrderedDict(
    ('tab20:' + name, value) for name, value in TAB20_SHADED_COLORS
)

# add light tableau colors to the list o named matplotlib colors
matplotlib.colors._colors_full_map.update(TAB20_SHADED_COLORS)


#
# Convenience methods for changing color appearance.
#
def _linear_interpolation(v1: float, v2: float, factor: float) -> float:
    return v1 + ((v2 - v1) * factor)


def blend(color1, color2, factor: float = 0.5):
    r1, g1, b1 = to_rgb(color1)
    r2, g2, b2 = to_rgb(color2)
    r_blend = _linear_interpolation(r1, r2, factor)
    g_blend = _linear_interpolation(g1, g2, factor)
    b_blend = _linear_interpolation(b1, b2, factor)
    return (r_blend, g_blend, b_blend)


def complement(color):
    rgb = to_rgb(color)
    k = sum([max(*rgb), min(*rgb)])
    r_comp, g_comp, b_comp = [k - v for v in rgb]
    return (r_comp, g_comp, b_comp)


def grayscale(color):
    r, g, b = to_rgb(color)
    weighted_average = 0.299 * r + 0.587 * g + 0.114 * b
    return (weighted_average, weighted_average, weighted_average)


def invert(color):
    rgb = to_rgb(color)
    r_inv, g_inv, b_inv = [1.0 - v for v in rgb]
    return (r_inv, g_inv, b_inv)


def shade(color, factor: float):
    return blend(color, 'black', factor)


def tint(color, factor: float):
    return blend(color, 'white', factor)


def tone(color, factor: float):
    return blend(color, 'gray', factor)

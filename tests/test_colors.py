#%%
import figure_tools  # type: ignore
import matplotlib.colors


#%%
def test_light_tableau_colors():
    assert matplotlib.colors.is_color_like('tab:lightblue')
    assert matplotlib.colors.is_color_like('tab:lightorange')
    assert matplotlib.colors.is_color_like('tab:lightgreen')
    assert matplotlib.colors.is_color_like('tab:lightred')
    assert matplotlib.colors.is_color_like('tab:lightpurple')
    assert matplotlib.colors.is_color_like('tab:lightbrown')
    assert matplotlib.colors.is_color_like('tab:lightpink')
    assert matplotlib.colors.is_color_like('tab:lightgray')
    assert matplotlib.colors.is_color_like('tab:lightolive')
    assert matplotlib.colors.is_color_like('tab:lightcyan')


def test_tab20_shaded_colors():
    assert matplotlib.colors.is_color_like('tab20:indigo2')


def test_default_tint():
    color = (0.5, 0.5, 0.5)
    tinted = figure_tools.colors.tint(color)
    assert tinted == [1.3 * 0.5, 1.3 * 0.5, 1.3 * 0.5]


def test_custom_tint():
    color = (0.5, 0.5, 0.5)
    tinted = figure_tools.colors.tint(color, factor=0.5)
    assert tinted == [1.5 * 0.5, 1.5 * 0.5, 1.5 * 0.5]


def test_tint_iterations():
    color = (0.5, 0.5, 0.5)
    tinted = figure_tools.colors.tint(color, factor=0.5, iterations=3)
    assert tinted == [0.9375, 0.9375, 0.9375]


def test_default_shade():
    color = (0.5, 0.5, 0.5)
    shaded = figure_tools.colors.shade(color)
    assert shaded == [0.7 * 0.5, 0.7 * 0.5, 0.7 * 0.5]


def test_custom_shade():
    color = (0.5, 0.5, 0.5)
    shaded = figure_tools.colors.shade(color, factor=0.5)
    assert shaded == [0.5 * 0.5, 0.5 * 0.5, 0.5 * 0.5]


def test_shade_iterations():
    color = (0.5, 0.5, 0.5)
    shaded = figure_tools.colors.shade(color, factor=0.5, iterations=3)
    assert shaded == [0.5**3 * 0.5, 0.5**3 * 0.5, 0.5**3 * 0.5]

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
#%%
import matplotlib.pyplot as plt
import numpy as np
from figure_tools import apply_style, create_figure, save_figure

# %%
apply_style()

# %%
fig = create_figure()

axes = fig.subplots(ncols=2, nrows=3)

x = np.linspace(-6, 6, 100)
y = np.sin(x)

plt.plot(x, y)

plt.tight_layout()
save_figure(__file__)

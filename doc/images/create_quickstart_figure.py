#%%
import numpy as np
import matplotlib.pyplot as plt
from figure_tools import apply_style, create_figure, save_figure

# %%
apply_style()

# %%
fig = create_figure(width='2x')

# ... put your own plotting logic here
# ...
# ...
x = np.linspace(0, 10, 50)
plt.plot(x, np.sin(x))
# ...
# ...
# ...

plt.tight_layout()

# Save the current figure in "png" format. The image will have the same
# name as the python script, except for another suffix.
save_figure(__file__)

# %%

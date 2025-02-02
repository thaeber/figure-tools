# %%
import numpy as np
import matplotlib.pyplot as plt
from figure_tools import apply_style, create_figure, save_figure, print_image_metadata

# %%
apply_style()

# %%
fig = create_figure(width='1x')

# ... put your own plotting logic here
# ...
# ...
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.sin(2.3 * x), '-')
plt.xlabel('$t$ / s')
plt.ylabel('amplitude')
plt.title('awesome figure title')
# ...
# ...
# ...

plt.tight_layout()

# Save the current figure in "png" format. The image will have the same
# name as the python script, except for another suffix.
save_figure(__file__)

# %%
print_image_metadata(__file__)

# %%

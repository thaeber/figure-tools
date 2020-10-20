#%%
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from figure_tools import apply_style, create_figure, save_figure
from figure_tools.save import _get_commit_hash

#%%
apply_style()

# %%
x = np.linspace(0, 10, 50)
plt.plot(x, np.sin(x), '.-')
save_figure(__file__,
            metadata={
                'git-commit': f'{_get_commit_hash()}',
                'filename': Path(__file__).name,
            })
plt.show()

# %%
from PIL import Image

img = Image.open(Path(__file__).with_suffix('.png'))
img.info
# %%

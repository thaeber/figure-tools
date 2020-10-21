![Python build and test](https://github.com/thaeber/figure-tools/workflows/Python%20build%20and%20test/badge.svg?branch=main)

# figure-tools
A small Python package for setting up a consistent workflow for creating images in scientific publications with matplotlib and with research data management (RDM) in mind.

## Installation

Install the package using `pip`

```shell
pip install git+https://github.com/thaeber/figure-tools.git#egg=figure-tools
```

or `conda`, by utilizing the pip support in the `environment.yml` file:

```yaml
name: <env-name>
channels:
  - defaults
dependencies:
  - python
  - pip
  # list of additional packages
  - pip:
      - git+https://github.com/thaeber/figure-tools.git#egg=figure-tools
```

## Quickstart

> We assume that all scripts for creating the figures are managed in
> a git repository to help in research data management.

Creating and saving figures always follows the same workflow:

```python
import numpy as np
import matplotlib.pyplot as plt
from figure_tools import apply_style, create_figure, save_figure

# Apply a common style and figure size. For example, the default
# figure size might be valid for a single column figure in a journal.
apply_style()

# Create a new figure that is one column wide (1x) and has 
# the default height.
fig = create_figure(width='1x')

# ... put your own plotting logic here
# ...
# ...
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.sin(2.3 * x), '-')
plt.xlabel('$t$ / s')
plt.ylabel('amplitude')
# ...
# ...
# ...

plt.tight_layout()

# Save the current figure in "png" format. The image will have the same
# name as the python script, except for another suffix.
save_figure(__file__)
```

This will create the following figure:

![Quickstart Figure](doc/images/create_quickstart_figure.png)

By default the package will add the git tag and commit hash (as obtained by `git describe --always`) as well as the script name (the `__file__` parameter above) to the figure as annotation. This behavior can be configured by environment variables.

The same information is passed to the `metadata` parameter of `fig.savefig`, so it can be retrieved later, e.g. with the `pillow` package and the `Image.info` field. Additionally, the metadata contains the output of `git blame` for the script file, so that the changes made to the figure can traced back to the individual commits. The `load_image_metadata` and `print_image_metadata` functions can be used to load or directly output the metadata. Internally the functions use the `Image.info` field of the `pillow` package. The output of `print_image_metadata` for the above image yields:

```yaml
       Software: Matplotlib version3.3.2, https://matplotlib.org/
        created: 2020-10-21 12:32:33.083226+00:00
     git-commit: v0.2.0-1-gca2bc9d-dirty
script-filename: create_quickstart_figure.py
      git-blame: ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  1) #%%
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  1) #%%
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  2) import numpy as np
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  3) import matplotlib.pyplot as plt
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  4) from figure_tools import apply_style, create_figure, save_figure
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  5) 
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  6) # %%
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  7) apply_style()
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  8) 
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200  9) # %%
                 00000000 (Not Committed Yet 2020-10-21 14:32:33 +0200 10) fig = create_figure(width='1x')
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 11) 
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 12) # ... put your own plotting logic here
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 13) # ...
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 14) # ...
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 15) x = np.linspace(0, 10, 50)
                 00000000 (Not Committed Yet 2020-10-21 14:32:33 +0200 16) plt.plot(x, np.sin(x), '.-')
                 00000000 (Not Committed Yet 2020-10-21 14:32:33 +0200 17) plt.plot(x, np.sin(2.3 * x), '.-')
                 00000000 (Not Committed Yet 2020-10-21 14:32:33 +0200 18) plt.xlabel('$t$ / s')
                 00000000 (Not Committed Yet 2020-10-21 14:32:33 +0200 19) plt.ylabel('amplitude')
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 20) # ...
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 21) # ...
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 22) # ...
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 23) 
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 24) plt.tight_layout()
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 25) 
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 26) # Save the current figure in "png" format. The image will have the same
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 27) # name as the python script, except for another suffix.
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 28) save_figure(__file__)
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 29) 
                 ca2bc9df (thaeber           2020-10-21 14:29:39 +0200 30) # %%
            dpi: (600, 600)
```

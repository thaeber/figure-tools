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


# OptiVision

Image Processing Library for Python. Implements a variety of image processing algorithms from scratch.

---

> **Note**: This library is just a fun project to learn about image processing and computer vision algorithms from scratch and to enhance my understanding of the concepts.


---
Various implemenatations of image processing algorithms from scratch using Python has been implemented in [this repository](https://github.com/Preet-Sojitra/DIP) as part of Digital Image Processing course at my university.

---
## Installation

```bash
pip install optivision
```

## Usage

```python
from PIL import Image
from optivision.transformations.logarithmic import logarithmic_transform
import numpy as np

# Load image
img = Image.open('path/to/image.jpg')

# Convert image to numpy array
img = np.array(img)

# Apply logarithmic transformation
img = logarithmic_transform(img, c=3)

# Convert numpy array to image
img = Image.fromarray(img)

# show image
img.show()
```

## Documentation

The official documentation is hosted on [Read the Docs](https://optivision.readthedocs.io/en/latest/index.html).


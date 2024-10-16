# EOF Analysis

This repository contains a Python implementation of Empirical Orthogonal Function (EOF) analysis, a widely used technique in climate and atmospheric sciences to extract dominant spatial patterns from geophysical datasets.

## Features
- **EOF Analysis**: Perform Principal Component Analysis (PCA) on gridded data to identify modes of variability.
- **Handles Latitude Weighting**: Accounts for the cosine of latitude to apply proper area weighting.
- **North Criterion**: Implements the North et al. criterion for determining the significance of modes.
- **Customizable**: Allows for PCA to be performed on either the covariance matrix or the correlation matrix.

## Requirements

Make sure you have the following Python packages installed:

- `numpy`
- `scipy`

You can install the dependencies by running:

```bash
pip install numpy scipy
```

### Example

```python
import numpy as np
from eof_analysis import perform_eof_analysis

# Example data: a 3D numpy array of shape [time, lat, lon]
# Replace this with your actual dataset
dat = np.random.rand(100, 20, 30)  # e.g., 100 time steps, 20 latitudes, 30 longitudes
lati = np.linspace(-90, 90, 20)  # 20 latitude points
loni = np.linspace(0, 360, 30)   # 30 longitude points

# Perform EOF analysis
score, latent, loading, north = perform_eof_analysis(dat, lati, loni)

# View results
print("Principal component time series (scores):", score)
print("Eigenvalues (latent):", latent)
print("EOF loading patterns:", loading)
print("North criterion results:", north)
```

## Authors

- Husile Bai ([husile.bai@vanderbilt.edu](mailto:husile.bai@vanderbilt.edu))
- Chayan Roychoudhury ([croychoudhury@arizona.edu](mailto:croychoudhury@arizona.edu))



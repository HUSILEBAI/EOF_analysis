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

Usage

The primary function in this repository is perform_eof_analysis(). Below is a breakdown of its inputs and outputs.
Function: perform_eof_analysis

python

def perform_eof_analysis(dat, lati, loni, flag=2, nmodes=10):
    """
    Perform EOF analysis on the provided dataset.

    Parameters:
    dat: np.ndarray
        The 3D dataset to analyze, with dimensions [time, lat, lon].
    lati: np.ndarray
        The latitude array corresponding to the dataset's grid.
    loni: np.ndarray
        The longitude array corresponding to the dataset's grid.
    flag: int, optional (default=2)
        Determines whether to perform PCA on the covariance matrix (flag=1) or on the correlation matrix (flag=2).
    nmodes: int, optional (default=10)
        The number of principal components (PCs) or EOF modes to calculate.

    Returns:
    score: np.ndarray
        The time series of each PC in a column.
    latent: np.ndarray
        The eigenvalue of each PC normalized to sum to 1.
    loading: np.ndarray
        The loading matrix of EOFs, with shape [nmodes, nlat, nlon].
    north: np.ndarray
        The North et al. criterion values for the first nmodes.
    """

Example

python

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

Repository Contents

    eof_analysis.py: Contains the main perform_eof_analysis function for EOF analysis.
    README.md: This readme file explaining the code and usage.
    LICENSE: The repository license (MIT License by default).

License

This project is licensed under the MIT License. See the LICENSE file for details.

Happy EOF-ing!

sql


You can copy this content into your `README.md` file in your local repository. Let me know if you need further help!



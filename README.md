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




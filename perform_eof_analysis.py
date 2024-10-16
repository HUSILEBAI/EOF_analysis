import numpy as np
from scipy.linalg import svd

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
    
    # Extract the dimensions of the data: time (nt), latitude (nlat), longitude (nlon)
    nt, nlat, nlon = dat.shape

    # Convert 1D latitude/longitude to 2D grids if needed
    if lati.ndim == 1:
        print("Converting lati and loni to 2D grids.")
        loni, lati = np.meshgrid(loni, lati)

    # Latitude weighting factor (cosine of latitude)
    wf = np.sqrt(np.cos(np.deg2rad(lati)))

    # Repeat the weighting factor across the time dimension
    wf = np.tile(wf, (nt, 1, 1))

    # Apply the latitude weighting to the data
    dat = dat * wf

    # Reshape the data into [time x (lat * lon)] for PCA
    dat = dat.reshape(nt, -1)

    # Center the data by removing the mean
    dat -= np.mean(dat, axis=0)

    # Standardize the data if performing PCA on the correlation matrix (flag == 2)
    if abs(flag) == 2:
        s = np.std(dat, axis=0)
        s[s == 0] = 1  # Prevent division by zero
        dat /= s

    # Perform Singular Value Decomposition (SVD)
    U, s, Vt = svd(dat / np.sqrt(nt - 1), full_matrices=False)

    # North et al. criterion for determining significant modes
    gg = s ** 2
    north = np.zeros((nmodes + 1, 4))
    north[:, 0] = gg[:nmodes + 1]  # Eigenvalues
    north[:, 1] = gg[:nmodes + 1] * np.sqrt(2 / nt)  # Uncertainty

    # Compute upper and lower bounds for the North criterion
    check = np.zeros((nmodes + 1, 2))
    check[:, 0] = gg[:nmodes + 1] + north[:, 1]
    check[:, 1] = gg[:nmodes + 1] - north[:, 1]

    # Apply the North criterion
    north[0, 2] = check[0, 1] > check[1, 0]
    for i in range(1, nmodes):
        north[i, 2] = (check[i, 0] < check[i - 1, 1]) & (check[i, 1] > check[i + 1, 0])

    # Calculate differences for North criterion
    delta = np.diff(north[:, 0])
    north[:-1, 3] = np.abs(delta / north[:-1, 1])

    # Project data onto the principal components (EOFs)
    score = dat @ Vt.T

    # Eigenvalues (latent) normalized to sum to 1
    latent_raw = s ** 2
    latent = latent_raw / np.sum(latent_raw)

    # Reshape the first nmodes of EOFs into [lat x lon]
    loading = np.full((nmodes, nlat, nlon), np.nan)
    for i in range(min(nmodes, Vt.shape[0])):
        loading[i, :] = Vt[i, :].reshape(nlat, nlon)

    return score, latent, loading, north

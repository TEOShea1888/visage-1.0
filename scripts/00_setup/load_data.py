"""
load_data.py
------------
Functions for loading input datasets for ViSAGE 1.0.
"""

import geopandas as gpd
import pandas as pd

def load_origins(path):
    """Load origin points (e.g., population-weighted centroids)."""
    return gpd.read_file(path)

def load_destinations(path):
    """Load greenspace polygons or centroids."""
    return gpd.read_file(path)

def load_network(path):
    """Load road or walking network."""
    return gpd.read_file(path)

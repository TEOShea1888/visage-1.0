"""
utils.py
--------
Shared helper functions for ViSAGE 1.0.
"""

def normalise(series):
    """Normalise a pandas Series to 0–1."""
    return (series - series.min()) / (series.max() - series.min())

"""
prepare_layers.py
-----------------
Data cleaning, CRS alignment, and attribute preparation.
"""

def align_crs(origins, destinations, network):
    """Ensure all layers share a common CRS."""
    target = origins.crs
    return (
        origins.to_crs(target),
        destinations.to_crs(target),
        network.to_crs(target)
    )

def normalise_attributes(df, columns):
    """Normalise selected columns to 0–1 scale."""
    for col in columns:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df

"""
gravity_model.py
----------------
Core gravity model for ViSAGE 1.0.
"""

import numpy as np

def gravity_weight(distance, beta):
    """Compute distance decay weight."""
    return np.exp(beta * distance)

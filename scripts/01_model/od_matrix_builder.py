"""
od_matrix_builder.py
--------------------
Builds the origin–destination matrix for ViSAGE 1.0.
"""

import numpy as np

def build_od_matrix(origins, destinations, distances):
    """Compute OD flows based on gravity weights and attractiveness."""
    flows = distances.copy()
    flows["flow"] = flows["weight"] * flows["attractiveness"]
    return flows

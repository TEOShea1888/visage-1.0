"""
quality_attractor.py
--------------------
Quality-based attractiveness extension for ViSAGE 1.0.
"""

def apply_quality_attractor(destinations, weight):
    """Multiply destination attractiveness by quality score."""
    destinations["attractiveness"] = destinations["quality"] * weight
    return destinations

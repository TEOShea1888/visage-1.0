"""
export_results.py
-----------------
Exports OD matrices, tables, and maps.
"""

def export_od_matrix(df, path):
    """Save OD matrix to CSV."""
    df.to_csv(path, index=False)

"""
scenario_runner.py
------------------
Generalised scenario runner for ViSAGE 1.0.
"""

def run_scenario(name, func):
    """Run a named scenario."""
    print(f"Running scenario: {name}")
    func()

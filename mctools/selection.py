"""
selection.py
Utility functions for working with component selection.
"""

import pyfbsdk


def list_all():
    """
    Returns a list of all components in the scene that are currently selected.
    """
    return [component for component in pyfbsdk.FBSystem().Scene.Components if component.Selected]

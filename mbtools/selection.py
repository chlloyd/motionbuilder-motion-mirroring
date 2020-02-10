"""
selection.py
Utility functions for working with component selection.
"""

from pyfbsdk import FBSystem


def list_all_selected():
    """Lists all components within the are that are selected.

    Returns:
        List: list of all components in the scene that are currently selected.

    """
    return [component for component in FBSystem().Scene.Components if component.Selected]


def list_all_by_type(object_type):
    """Lists all components in the scene by a type.

    Args:
        object_type (str): Type of object to select.

    Returns:
        List: All object in the scene by the type object_type.

    """
    # Get all nodes in scene and find joints
    allNodes = FBSystem().Scene.Components
    object_list = []
    for lComponent in allNodes:
        # print lComponent.Name
        if lComponent and lComponent.ClassName() == object_type:
            object_list.append(lComponent.LongName)
    return object_list

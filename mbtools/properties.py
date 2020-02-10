"""
properties.py
Utility functions for working with component properties.
"""

from pyfbsdk import FBVector3d


def get_rotation(object):
    """Gets the rotation property from an object.

    Args:
        object: An object in the scene.

    Returns: The rotation of an object.

    """
    return object.Rotation


def get_position(object):
    """Gets the position property from an object.

    Args:
        object: An object in the scene.

    Returns: The position of an object.

    """
    return object.Translation


def get_scale(object):
    """Gets the scale property from an object.

    Args:
        object: An object in the scene.

    Returns: The scale of an object.

    """
    return object.Scaling


def set_rotation(object, rotation):
    """Sets the rotation property on an object.

    Args:
        object: An object in the scene.
        rotation: (Tuple): (x, y, z) rotation data.

    Returns: None

    """
    object.Rotation = FBVector3d(rotation)


def set_position(object, position):
    """Sets the position property on an object.

    Args:
        object: An object in the scene.
        position: (Tuple): (x, y, z) position data.

    Returns: None

    """
    object.Rotation = FBVector3d(position)


def set_scale(object, scale):
    """Sets the scale property on an object.

    Args:
        object: An object in the scene.
        scale: (Tuple): (x, y, z) scale data.

    Returns: None

    """
    object.Rotation = FBVector3d(scale)

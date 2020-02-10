import sys
import os
import pyfbsdk

try:
    import mbtools as mb
except ImportError:
    MBTOOLS_PATH = os.path.dirname(os.path.realpath(__file__))
    if MBTOOLS_PATH not in sys.path:
        sys.path.append(MBTOOLS_PATH)
        import mbtools as mb

reload(mb)  # only here for when the library is be edited


# TODO: Add Comments on each line


def BuildUI():
    pass


def mirror_keyframes():
    """FOR frames in frame sequence:
        for rotation in joint:
            flip from hip joint (change_orientation, rotation)
            END FOR
        END FOR"""
    for frame in range(mb.time.first_frame(), mb.time.last_frame() + 1):
        for joint in mb.selection.list_all_by_type("FBModelSkeleton"):
            rotation = mb.properties.get_rotation(joint)
            new_rotation = (rotation[0] * -1, rotation[1], rotation[2])
            mb.properties.set_rotation(joint, new_rotation)


mirror_keyframes()

"""FUNC flip from hip joint (orientation, rotation):
    convert quaternion to rotation matrix
    mirror matrix on orientation
    convert rotation matrix to quaternion
    return new quaternion
    END FUNC"""

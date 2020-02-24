"""
joint.py
Utility functions for working with joint data.
"""

import os
#from pyfbsdk import FBScene
from mbtools import readdata


mirror_data = readdata._read_json_file(os.path.dirname(os.path.realpath(__file__)) + "/joint_mirror.json")


def joint_mirror(joint_to_mirror):
    """Finds the mirror joint from a parse through joint_mirror.json

    Args:
        joint_to_mirror:The joint to find the mirror of

    Returns:Mirror of the joint, else returns None

    """
    for joint in mirror_data:
        if joint["joint"] == joint_to_mirror:
            return joint["mirror"]

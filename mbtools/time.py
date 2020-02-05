"""
time.py
Utility functions for working with time data.
"""

from pyfbsdk import FBSystem, FBTime


def first_frame():
    """Returns the value of the first frame of the current take in the scene as an integer.

    Returns:
        int: First frame value of the scene

    """
    return FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()


def last_frame():
    """Returns the value of the last frame of the current take in the scene as an integer.

    Returns:
        int: Last frame value of the scene

    """
    return FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame()


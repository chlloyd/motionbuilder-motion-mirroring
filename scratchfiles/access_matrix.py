import os
import sys
import pyfbsdk

try:
    import mbtools as mb
except ImportError:
    MBTOOLS_PATH = os.path.dirname(os.path.realpath(__file__))
    if MBTOOLS_PATH not in sys.path:
        sys.path.append(MBTOOLS_PATH)
        import mbtools as mb

rotation_multiply = pyfbsdk.FBMatrix([(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, -1, 0), (0, 0, 0, 1)])

for joint in mb.selection.list_all_by_type("FBModelSkeleton"):
    joint_rotation_matrix = pyfbsdk.FBMatrix()
    joint.GetMatrix(joint_rotation_matrix)
    print(type(joint_rotation_matrix))
    print(type(joint_rotation_matrix))
    matrix_multiply = pyfbsdk.FBMatrixMult(joint_rotation_matrix, rotation_multiply)
    print(matrix_multiply)
    break

    # joint_matrix = FBMatrix(a)

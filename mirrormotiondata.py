import sys
import os
import json
import pyfbsdk

try:
    import mbtools as mb
except ImportError:
    MBTOOLS_PATH = os.path.dirname(os.path.realpath(__file__))
    if MBTOOLS_PATH not in sys.path:
        sys.path.append(MBTOOLS_PATH)
        import mbtools as mb


# TODO: Add Comments on each line


def BuildUI():
    pass


def mirror_keyframes():
    """FOR frames in frame sequence:
        for rotation in joint:
            flip from hip joint (change_orientation, rotation)
            END FOR
        END FOR"""
    data = {}
    # for frame in range(mb.time.first_frame(), mb.time.last_frame() + 1):
    # for joint in mb.selection.list_all_by_type("FBModelSkeleton"):
    #     joint_rotation = mb.properties.get_rotation(joint)
    #     data[joint.Name] = {"rotation": {"x": joint_rotation[0], "y": joint_rotation[1], "z": joint_rotation[2]}}

    #mb.readdata._write_json_file("G:\\Programming Projects\\motionbuilder-motion-mirroring\\test_json.json", data)

    rotation_data = mb.readdata._read_json_file("G:\\Programming Projects\\motionbuilder-motion-mirroring\\test_json.json")
    joint_list = []
    for joint, rotation in mb.readdata._read_json_file("G:\\Programming Projects\\motionbuilder-motion-mirroring\\test_json.json").items():
        print(joint)
        print(rotation)
    #     joint_list.append(joint)
    #
    # for joint in joint_list:
    #     print(rotation_data[joint])










        # rotation_node = joint.Rotation.GetAnimationNode()
        # if rotation_node == None:
        #     pass
        # else:
        #     print(rotation_node.Nodes[0].FCurve.Name)
        #     print(rotation_node.Nodes[1].FCurve.Name)
        #     print(rotation_node.Nodes[2].FCurve.Name)
        # rotation = mb.properties.get_rotation(joint)
        # new_rotation = (rotation[0] * -1, rotation[1], rotation[2])
        # mb.properties.set_rotation(joint, new_rotation)


mirror_keyframes()

"""FUNC flip from hip joint (orientation, rotation):
    convert quaternion to rotation matrix
    mirror matrix on orientation
    convert rotation matrix to quaternion
    return new quaternion
    END FUNC"""

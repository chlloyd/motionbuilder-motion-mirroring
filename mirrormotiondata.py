from pyfbsdk import FBComponentList, FBFindObjectsByName, FBModelSkeleton, FBFindModelByLabelName


def joint_mirror(joint_to_mirror):
    """Returns the mirrored joint name of arg: joint to mirror (LeftArm -> RightArm).

    Args:
        joint_to_mirror (str): Joint the needs mirroring.

    Returns:
         str: Mirrored joint name.
         None: If no there are no mirrored joint.

    """
    if "Left" in joint_to_mirror:
        return joint_to_mirror.replace("Left", "Right")
    elif "Right" in joint_to_mirror:
        return joint_to_mirror.replace("Right", "Left")
    elif "L_" in joint_to_mirror:
        return joint_to_mirror.replace("L_", "R_")
    elif "R_" in joint_to_mirror:
        return joint_to_mirror.replace("R_", "L_")
    elif "_L" in joint_to_mirror:
        return joint_to_mirror.replace("_L", "_R")
    elif "_R" in joint_to_mirror:
        return joint_to_mirror.replace("_R", "_L")
    elif "L" in joint_to_mirror and "Lower" not in joint_to_mirror:
        return joint_to_mirror.replace("L", "R")
    elif "R" in joint_to_mirror:
        return joint_to_mirror.replace("R", "L")
    else:
        return None


def select_by_namespace(namespace):
    """Selects all joints within a namespace.

    Args:
        namespace (str): Namespace to select

    Returns:
        list: Joints with selected namespace

    """
    foundComponents = FBComponentList()
    includeNamespace = True
    modelsOnly = False
    FBFindObjectsByName(namespace, foundComponents, includeNamespace, modelsOnly)
    components_list = []
    for component in foundComponents:
        components_list.append(component)
    return components_list


def mirror(plane, skeleton_namespace):
    """Main function to mirror joints.

    Args:
        plane (str): The plane to mirror joints on
        skeleton_namespace (str): Namespace to passthrough to select_by_namespace function

    """
    # Creating multiplier for each selected plane to mirror e.g. XY negates Y and Z rotations and X translation
    if plane == "XY":
        negation = {"rotation": (1, -1, -1), "translation": (-1, 1, 1)}  # negate rotation YZ, translation X
    elif plane == "YZ":
        negation = {"rotation": (-1, 1, -1), "translation": (1, -1, 1)}  # negate rotation XZ, translation Y
    elif plane == "XZ":
        negation = {"rotation": (-1, -1, 1), "translation": (1, 1, -1)}  # negate rotation XY, translation Z

    # Get all joint in a namespace
    skeleton = select_by_namespace(skeleton_namespace)
    rotation_data = {}
    translation_data = {}

    for joint in skeleton:  # Iterates over the joints to gather all keyframes
        if type(joint) == FBModelSkeleton:
            try:
                animRotateNode = joint.Rotation.GetAnimationNode()

                # X Orientation
                xOrentationList = []
                fcurveRotateX = animRotateNode.Nodes[0].FCurve.Keys
                for curve in fcurveRotateX:
                    xOrentationList.append((curve.Time, curve.Value))

                # Y Orientation
                yOrentationList = []
                fcurveRotateY = animRotateNode.Nodes[1].FCurve.Keys
                for curve in fcurveRotateY:
                    yOrentationList.append((curve.Time, curve.Value))

                # Z Orientation
                zOrentationList = []
                fcurveRotateZ = animRotateNode.Nodes[2].FCurve.Keys
                for curve in fcurveRotateZ:
                    zOrentationList.append((curve.Time, curve.Value))

                # Saves the rotation keyframes into a dictionary of lists
                rotation_data[joint] = {"x": xOrentationList, "y": yOrentationList, "z": zOrentationList}

            except AttributeError:
                # Passes past joints without any rotation animation nodes
                pass

            try:
                # Looks for translation animation nodes
                animTranslateNode = joint.Translation.GetAnimationNode()

                # X Orientation
                xOrentationList = []
                fcurveTranslateX = animTranslateNode.Nodes[0].FCurve.Keys
                for curve in fcurveTranslateX:
                    xOrentationList.append((curve.Time, curve.Value))

                # Y Orientation
                yOrentationList = []
                fcurveTranslateY = animTranslateNode.Nodes[1].FCurve.Keys
                for curve in fcurveTranslateY:
                    yOrentationList.append((curve.Time, curve.Value))

                # Z Orientation
                zOrentationList = []
                fcurveTranslateZ = animTranslateNode.Nodes[2].FCurve.Keys
                for curve in fcurveTranslateZ:
                    zOrentationList.append((curve.Time, curve.Value))

                # Saves the translation keyframes into a dictionary
                translation_data[joint] = {"x": xOrentationList, "y": yOrentationList, "z": zOrentationList}

            except AttributeError:
                # Passes past joints without any translation animation nodes
                pass

    # Iterates over all data in rotation_data
    for joint, data in rotation_data.items():

        # Finds a joints mirror joint
        if joint_mirror(joint.Name) is None:
            selected_joint = FBFindModelByLabelName(joint.LongName)
        else:
            selected_joint = FBFindModelByLabelName(joint_mirror(joint.LongName))

        animNode = selected_joint.Rotation.GetAnimationNode()

        # Sets new keyframes to X Rotation
        fcurve = animNode.Nodes[0].FCurve
        for xValue in data["x"]:
            fcurve.KeyAdd(xValue[0], negation["rotation"][0] * xValue[1])

        # Sets new keyframes to Y Rotation
        fcurve = animNode.Nodes[1].FCurve
        for yValue in data["y"]:
            fcurve.KeyAdd(yValue[0], negation["rotation"][1] * yValue[1])

        # Sets new keyframes to Z Rotation
        fcurve = animNode.Nodes[2].FCurve
        for zValue in data["z"]:
            fcurve.KeyAdd(zValue[0], negation["rotation"][2] * zValue[1])

    # Iterates over all data in translation_data
    for joint, data in translation_data.items():

        animNode = joint.Translation.GetAnimationNode()

        # Sets new keyframes to X translation
        fcurve = animNode.Nodes[0].FCurve
        for xValue in data["x"]:
            fcurve.KeyAdd(xValue[0], negation["translation"][0] * xValue[1])

        # Sets new keyframes to Y translation
        fcurve = animNode.Nodes[1].FCurve
        for yValue in data["y"]:
            fcurve.KeyAdd(yValue[0], negation["translation"][1] * yValue[1])

        # Sets new keyframes to Z translation
        fcurve = animNode.Nodes[2].FCurve
        for zValue in data["z"]:
            fcurve.KeyAdd(zValue[0], negation["translation"][2] * zValue[1])

mirror("XY", "BVH:*")

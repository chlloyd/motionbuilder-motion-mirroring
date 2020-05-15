from pyfbsdk import FBComponentList, FBFindObjectsByName, FBModelSkeleton, FBFindModelByLabelName


def joint_mirror(joint_to_mirror):
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
    foundComponents = FBComponentList()
    includeNamespace = True
    modelsOnly = False
    FBFindObjectsByName(namespace, foundComponents, includeNamespace, modelsOnly)
    components_list = []
    for component in foundComponents:
        components_list.append(component)
    return components_list


def mirror(plane, skeleton_namespace):
    if plane == "XY":
        negation = {"rotation": (1, -1, -1), "translation": (-1, 1, 1)}  # negate rotation YZ, translation X
    elif plane == "YZ":
        negation = {"rotation": (-1, 1, -1), "translation": (1, -1, 1)}  # negate rotation XZ, translation Y
    elif plane == "XZ":
        negation = {"rotation": (-1, -1, 1), "translation": (1, 1, -1)}  # negate rotation XY, translation Z

    skeleton = select_by_namespace(skeleton_namespace)
    rotation_data = {}
    translation_data = {}
    for joint in skeleton:
        if type(joint) == FBModelSkeleton:
            try:
                animRotateNode = joint.Rotation.GetAnimationNode()

                xOrentationList = []
                fcurveRotateX = animRotateNode.Nodes[0].FCurve.Keys
                for curve in fcurveRotateX:
                    xOrentationList.append((curve.Time, curve.Value))

                yOrentationList = []
                fcurveRotateY = animRotateNode.Nodes[1].FCurve.Keys
                for curve in fcurveRotateY:
                    yOrentationList.append((curve.Time, curve.Value))

                zOrentationList = []
                fcurveRotateZ = animRotateNode.Nodes[2].FCurve.Keys
                for curve in fcurveRotateZ:
                    zOrentationList.append((curve.Time, curve.Value))

                rotation_data[joint] = {"x": xOrentationList, "y": yOrentationList, "z": zOrentationList}

            except AttributeError:
                pass

            try:
                animTranslateNode = joint.Translation.GetAnimationNode()

                xOrentationList = []
                fcurveTranslateX = animTranslateNode.Nodes[0].FCurve.Keys
                for curve in fcurveTranslateX:
                    xOrentationList.append((curve.Time, curve.Value))

                yOrentationList = []
                fcurveTranslateY = animTranslateNode.Nodes[1].FCurve.Keys
                for curve in fcurveTranslateY:
                    yOrentationList.append((curve.Time, curve.Value))

                zOrentationList = []
                fcurveTranslateZ = animTranslateNode.Nodes[2].FCurve.Keys
                for curve in fcurveTranslateZ:
                    zOrentationList.append((curve.Time, curve.Value))

                translation_data[joint] = {"x": xOrentationList, "y": yOrentationList, "z": zOrentationList}

            except AttributeError:
                pass

    for joint, data in rotation_data.items():
        if joint_mirror(joint.Name) is None:
            selected_joint = FBFindModelByLabelName(joint.LongName)
        else:
            selected_joint = FBFindModelByLabelName(joint_mirror(joint.LongName))

        animNode = selected_joint.Rotation.GetAnimationNode()
        fcurve = animNode.Nodes[0].FCurve
        for xValue in data["x"]:
            fcurve.KeyAdd(xValue[0], negation["rotation"][0] * xValue[1])

        fcurve = animNode.Nodes[1].FCurve
        for yValue in data["y"]:
            fcurve.KeyAdd(yValue[0], negation["rotation"][1] * yValue[1])

        fcurve = animNode.Nodes[2].FCurve
        for zValue in data["z"]:
            fcurve.KeyAdd(zValue[0], negation["rotation"][2] * zValue[1])

    for joint, data in translation_data.items():

        animNode = joint.Translation.GetAnimationNode()
        fcurve = animNode.Nodes[0].FCurve
        for xValue in data["x"]:
            fcurve.KeyAdd(xValue[0], negation["translation"][0] * xValue[1])
        fcurve = animNode.Nodes[1].FCurve
        for yValue in data["y"]:
            fcurve.KeyAdd(yValue[0], negation["translation"][1] * yValue[1])
        fcurve = animNode.Nodes[2].FCurve
        for zValue in data["z"]:
            fcurve.KeyAdd(zValue[0], negation["translation"][2] * zValue[1])

# mirror("XY", "BVH:*")

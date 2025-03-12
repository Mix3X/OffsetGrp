# Maya Script: Create Offset and SDK Groups for Selected Controllers

This Python script for Autodesk Maya creates offset and SDK (Set Driven Key) groups for selected NURBS curve controllers whose names end with `_Ctrl`. It automates the creation and hierarchy setup for rigging purposes.

## Features

- **Automatic Group Creation:** Generates two groups for each selected controller:
  - An **Offset Group** (named with `_Offset_Grp`)
  - An **SDK Group** (named with `_SDK_Grp`)
- **Hierarchy Setup:** Parents the controller under the SDK group, which is nested in the Offset group.
- **Alignment:** Ensures the groups match the controller's world transform.
- **Error Handling:** Warns if selected objects don’t follow the naming convention.

## Requirements

- Autodesk Maya 2022 or newer

## Usage

1. Select the NURBS curve controllers you want to group (names must end with `_Ctrl`).
2. Run the script in the Maya Script Editor.
3. The script will create and align Offset and SDK groups for each controller.

## Example

If you select controllers named:

- `arm_Ctrl`
- `leg_Ctrl`

The following groups will be created and parented correctly:

- `arm_Offset_Grp`
  - `arm_SDK_Grp`
    - `arm_Ctrl`
- `leg_Offset_Grp`
  - `leg_SDK_Grp`
    - `leg_Ctrl`

## Code

```python
import maya.cmds as cmds

def create_groups_for_selected_curves():
    # Get selected curves
    selected_curves = cmds.ls(selection=True, type='transform')

    if not selected_curves:
        cmds.error("No curves selected. Please select control curves.")
        return

    for ctrl in selected_curves:
        # Check if name ends with _Ctrl
        if not ctrl.endswith("_Ctrl"):
            cmds.warning(f"Object '{ctrl}' does not appear to be a controller (_Ctrl missing).")
            continue

        # Create group names
        offset_grp_name = ctrl.replace("_Ctrl", "_Offset_Grp")
        sdk_grp_name = ctrl.replace("_Ctrl", "_SDK_Grp")

        # Create groups
        offset_grp = cmds.group(empty=True, name=offset_grp_name)
        sdk_grp = cmds.group(empty=True, name=sdk_grp_name)

        # Align groups to controller
        cmds.delete(cmds.parentConstraint(ctrl, offset_grp))
        cmds.delete(cmds.parentConstraint(ctrl, sdk_grp))

        # Parent hierarchy
        cmds.parent(sdk_grp, offset_grp)
        cmds.parent(ctrl, sdk_grp)

        print(f"Groups created and aligned for: {ctrl}\n  - {offset_grp}\n  - {sdk_grp}")

# Run the function
create_groups_for_selected_curves()
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.




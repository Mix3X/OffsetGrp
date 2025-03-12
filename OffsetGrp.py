import maya.cmds as cmds

def create_groups_for_selected_curves():
    # Obtenir la sélection
    selected_curves = cmds.ls(selection=True, type='transform')

    if not selected_curves:
        cmds.error("Aucune courbe sélectionnée. Veuillez sélectionner des courbes de contrôle.")
        return

    for ctrl in selected_curves:
        # Vérifier si le nom contient le suffixe _Ctrl
        if not ctrl.endswith("_Ctrl"):
            cmds.warning(f"L'objet '{ctrl}' ne semble pas être un contrôleur (_Ctrl manquant).")
            continue

        # Créer les noms des groupes
        offset_grp_name = ctrl.replace("_Ctrl", "_Offset_Grp")
        sdk_grp_name = ctrl.replace("_Ctrl", "_SDK_Grp")

        # Créer les groupes
        offset_grp = cmds.group(empty=True, name=offset_grp_name)
        sdk_grp = cmds.group(empty=True, name=sdk_grp_name)

        # Aligner les transformations des groupes sur le contrôleur
        cmds.delete(cmds.parentConstraint(ctrl, offset_grp))
        cmds.delete(cmds.parentConstraint(ctrl, sdk_grp))

        # Hiérarchiser les groupes
        cmds.parent(sdk_grp, offset_grp)
        cmds.parent(ctrl, sdk_grp)

        print(f"Groupes créés et alignés pour : {ctrl}\n  - {offset_grp}\n  - {sdk_grp}")

# Appeler la fonction
create_groups_for_selected_curves()
import bpy
from ...helpers.constants import SynchOperatorConstants


# Synchs the data names to match the name of the object
class SynchDataNameOperator(bpy.types.Operator):
    bl_idname = SynchOperatorConstants.ID
    bl_label = SynchOperatorConstants.LABEL
    bl_description = "Will iterate through all selected objects and will rename the name of the data object to match the object's name"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        selected_objects = context.selected_objects

        for object in selected_objects:
            object.data.name = object.name
        return {"FINISHED"}

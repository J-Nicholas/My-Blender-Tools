import bpy
from . constants import SynchOperatorConstants

# Synchs the data names to match the name of the object
class SynchDataNameUseCase(bpy.types.Operator):
    bl_idname = SynchOperatorConstants.id
    bl_label = SynchOperatorConstants.label
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        selected_objects = context.selected_objects

        for object in selected_objects:
            object.data.name = object.name
        return {"FINISHED"}

import bpy
from ...helpers.constants import SynchOperatorConstants


class RiggingPanel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_rigging_panel"
    bl_label = "Rigging Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My Tools"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator(
            operator=SynchOperatorConstants.ID,
            text=SynchOperatorConstants.LABEL,
            icon="OUTLINER_DATA_FONT",
        )

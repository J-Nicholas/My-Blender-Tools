bl_info = {
    "name": "My Tools Addon",
    "author": "Johnathan Nicholas",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "Panel",
    "description": "Various Utils",
    "category": "Object",
}

import bpy
from .blender import SynchDataNameOperator, RiggingPanel

# classes = NAME_SYNCH_CLASSES


def register():
    bpy.utils.register_class(SynchDataNameOperator)
    bpy.utils.register_class(RiggingPanel)
    # for clazz in classes:
    # bpy.utils.register_class(clazz)


def unregister():
    bpy.utils.unregister_class(RiggingPanel)
    bpy.utils.unregister_class(SynchDataNameOperator)
    # for clazz in classes:
    #     bpy.utils.unregister_class(clazz)

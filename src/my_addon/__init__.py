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
from blender import CLASSES as NAME_SYNCH_CLASSES

classes = (NAME_SYNCH_CLASSES,)


def register():
    for clazz in classes:
        bpy.utils.register_class(clazz)


def unregister():
    for clazz in classes:
        bpy.utils.unregister_class(clazz)

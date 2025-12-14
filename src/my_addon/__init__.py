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

classes = []
try:
    from .blender import CLASSES as NAME_SYNCH_CLASSES

    classes = [NAME_SYNCH_CLASSES]
except AttributeError:
    # pytest run, it can't resolve bpy things because it's just a fake module
    pass


def register():
    for clazz in classes:
        bpy.utils.register_class(clazz)


def unregister():
    for clazz in classes:
        bpy.utils.unregister_class(clazz)

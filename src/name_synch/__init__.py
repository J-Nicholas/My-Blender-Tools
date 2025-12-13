from .operators.name_syncher import SynchDataNameUseCase

__all__ = ["SynchDataNameUseCase"]

# convenience object to provide Blender with classes that it needs to register
# without having to change the signature each time this list changes
CLASSES = (SynchDataNameUseCase,)

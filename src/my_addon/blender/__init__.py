from .operators.name_synch_operator import SynchDataNameOperator

__all__ = ["SynchDataNameOperator"]

# convenience object to provide Blender with classes that it needs to register
# without having to change the signature each time this list changes
CLASSES = (SynchDataNameOperator,)

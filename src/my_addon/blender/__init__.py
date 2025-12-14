from .operators.name_synch_operator import SynchDataNameOperator
from .panels.my_panel import RiggingPanel

__all__ = ["SynchDataNameOperator", "RiggingPanel"]

# convenience object to provide Blender with classes that it needs to register
# without having to change the signature each time this list changes
CLASSES = [SynchDataNameOperator, RiggingPanel]

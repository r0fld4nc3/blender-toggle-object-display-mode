bl_info = {
    "name": "Toggle Wire Object Mode Display",
    "author": "Artur Rosário",
    "version": (0, 0, 1),
    "blender": (4, 2, 5),
    "location": "",
    "description": "Toggles Objects' Display Mode To Wire or Textured",
    "warning": "",
    "doc_url": "",
    "category": "Object"
}

import bpy
import importlib
from . import toggle_wire_mode_display

importlib.reload(toggle_wire_mode_display)


def register():
    toggle_wire_mode_display.register()


def unregister():
    toggle_wire_mode_display.unregister()


if __name__ == "__main__":
    register()

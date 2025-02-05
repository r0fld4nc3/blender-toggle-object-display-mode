import bpy

def toggle_wire_mode():
    wires = 0
    textureds = 0
    other = 0
    objects = [obj for obj in bpy.context.selected_objects if obj and obj.type == 'MESH']

    if not objects:
        return

    for obj in objects:
        if obj.display_type == 'WIRE':
            wires += 1
        elif obj.display_type == 'TEXTURED':
            textureds += 1
        else:
            other += 1  # SOLID, BOUNDING_BOX, or other modes

    if wires > textureds and textureds > 0:
        display_mode = 'WIRE'
    elif textureds > wires and wires > 0:
        display_mode = 'TEXTURED'
    elif other == len(objects):  # If all objects are neither wire nor textured
        display_mode = 'WIRE'
    else:
        display_mode = 'WIRE' if wires == 0 else 'TEXTURED'

    # Apply the new display type
    for obj in objects:
        obj.display_type = display_mode

class OBJECT_OT_toggle_wire(bpy.types.Operator):
    """Toggle Wire Display"""
    bl_idname = "object.toggle_wire_display_mode"
    bl_label = "Toggle Wire Display"

    def execute(self, context):
        toggle_wire_mode()
        return {'FINISHED'}
    
classes = [
    OBJECT_OT_toggle_wire
]

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if not kc:
        return
    
    # Check if the keymap entry already exists
    km = kc.keymaps.get("Object Mode")
    if not km:
        km = kc.keymaps.new(name="Object Mode", space_type='EMPTY')

    # Ensure there's no duplicate
    for kmi in km.keymap_items:
        if kmi.idname == "object.toggle_wire_display_mode":
            return
    
    # Create a new keybinding only if it doesn't exist
    kmi = km.keymap_items.new("object.toggle_wire_display_mode", type='FOUR', value='PRESS')
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_toggle_wire)

if __name__ == "__main__":
    register()

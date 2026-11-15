def main():
    net_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    ctx = net_editor.pwd()

    obj_merge = ctx.createNode('object_merge', force_valid_node_name=True)
    obj_merge.setPosition(hou.ui.paneTabUnderCursor().cursorPosition())

    selection = hou.selectedNodes()

    obj_merge.parm('numobj').set(max(len(selection), 1))

    obj_merge.setName("in_")

    if len(selection) != 0:
        obj_merge.setName("in_" + selection[0].name().replace('OUT_', ''), unique_name=True)

    for node in selection:
        index = selection.index(node)
        parm = obj_merge.parm(f'objpath{index+1}')
        parm.set(obj_merge.relativePathTo(node))
import hou

def getContext():
    net_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    ctx = net_editor.pwd()

    return net_editor, ctx



def null():
    net_editor, ctx = getContext()

    null = ctx.createNode('null', force_valid_node_name=True)
    null.setPosition(hou.ui.paneTabUnderCursor().cursorPosition())

    null.setName('OUT_', True)

    if len(hou.selectedNodes()) != 0:
        null.setName('OUT_' + hou.selectedNodes()[0].name(), unique_name=True)
        null.setInput(0, hou.selectedNodes()[0])



def obj_merge():
    net_editor, ctx = getContext()

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



def output():
    net_editor, ctx = getContext()

    output = ctx.createNode('output')
    output.setPosition(hou.ui.paneTabUnderCursor().cursorPosition())

    output.setName('OUTPUT_')

    if len(hou.selectedNodes()) != 0:
        output.setName('OUTPUT_' + hou.selectedNodes()[0].name().replace('OUT_', ''))
        output.setInput(0, hou.selectedNodes()[0])
        
    used_output_index = []
        
    for node in ctx.children():
        if node.type().name() == 'output':
            output_index = node.parm('outputidx').eval()
            used_output_index.append(output_index)
            
    for index in range(0, len(used_output_index)):
        if index not in used_output_index:
            output.parm('outputidx').set(index)
            break
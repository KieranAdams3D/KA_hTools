def main():
    net_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    ctx = net_editor.pwd()

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
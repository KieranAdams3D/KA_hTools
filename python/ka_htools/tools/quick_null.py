import hou

def main():
    net_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    ctx = net_editor.pwd()

    null = ctx.createNode('null', force_valid_node_name=True)
    null.setPosition(hou.ui.paneTabUnderCursor().cursorPosition())

    null.setName('OUT_', True)

    if len(hou.selectedNodes()) != 0:
        null.setName('OUT_' + hou.selectedNodes()[0].name(), unique_name=True)
        null.setInput(0, hou.selectedNodes()[0])
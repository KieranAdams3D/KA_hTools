import hou

def main():
    ne = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

    if (hou.updateModeSetting() == hou.updateMode.Manual):
        hou.setUpdateMode(hou.updateMode.AutoUpdate)
        ne.flashMessage('LOP_resampletransforms', 'Auto Update', 1)
        
    else:
        hou.setUpdateMode(hou.updateMode.Manual)
        ne.flashMessage('BUTTONS_stop', 'Manual', 1)
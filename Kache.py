import hou

class KA_Kache:
    def __init__(self):
        
        print('kache initialised')

        hip = self.findHIP()

    def findHIP(self):
        hip = hou.expandString("$HIP")
        return hip

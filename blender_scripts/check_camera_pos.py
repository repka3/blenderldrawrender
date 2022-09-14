import bpy

class CameraProp:
    def __init__(self,location,rotation):
        self.location=location
        self.rotation=rotation
def getCamera():
    camera_obj=None
    for ob in bpy.data.objects:
        if "camera" in ob.name.lower():
            camera_obj=ob
            break
    if camera_obj is None:
        raise Exception("No camera found")
    return camera_obj

def adjustCamera(camera_prop):
    #adjust camera
    camera_obj=getCamera()
    
    camera_obj.location = camera_prop.location
    #print(camera_obj.rotation_euler)
    camera_obj.rotation_euler = camera_prop.rotation
    
    
camera_props=[CameraProp((0, -0.45, -0.1),(1.5708, 0, 0)),
              CameraProp((0, -0.45, 0.0),(1.338671, 0, 0)),
              CameraProp((0.1, -0.47, -0.1),(1.5708, 0, 0.223402)),
              CameraProp((-0.1, -0.46, -0.05),(1.452118, 0, -0.209440)),
              CameraProp((0, -0.48, -0.09),(1.546365, 0, 0)),        
              CameraProp((0.0000, -0.4500, 0.0545),(1.2328, -0.0000, 0.0000)),
              CameraProp((0.0000, -0.4500, -0.1850),(1.7664884, -0.0000, 0.0000)),
              CameraProp((-0.11729514598846436,-0.41233405470848083,-0.18502339720726013),(1.770105,0.0,-0.25654974579811096)), #left bottom
              CameraProp((-0.11729514598846436,-0.41233405470848083,-0.10176825523376465),(1.5707963705062866,0.0,-0.24705058336257935)), #center left
              CameraProp((-0.11729514598846436,-0.41233405470848083,0.014333173632621765),(1.2870395183563232,0.0,-0.2726947069168091)), #left top
              CameraProp((0.08715380728244781,-0.41233405470848083,0.0795467421412468),(1.1581838130950928,0.0,0.23237425088882446)), #right top
              CameraProp((0.13598544895648956,-0.41233405470848083,-0.18502339720726013),(1.7636053562164307,-0.0,0.3226548731327057)), #right bottom
              CameraProp((0.13598544895648956,-0.41233405470848083,-0.10000000149011612),(1.5838364362716675,-0.0,0.3261455297470093)) #center right
              
              ]
              
adjustCamera(camera_props[10])

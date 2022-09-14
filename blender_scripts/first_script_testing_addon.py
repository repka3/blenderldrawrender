import bpy
from io_scene_lpub3d_importldraw.loadldraw import loadldraw
import os
class CameraProp:
    def __init__(self,location,rotation):
        self.location=location
        self.rotation=rotation

class LightProp:
    def __init__(self,location,energy):
        self.location=location
        self.energy=energy
 
class PlaneProp:
    def __init__(self,location,rotation,diffuse_color):
        self.location=location
        self.rotation=rotation
        self.diffuse_color=diffuse_color
               
def resetScene():
    
    obs_to_delete=[]    
    for ob in bpy.data.objects:
        #print (ob.name)
        if ob.name.endswith('.dat') or "cube" in ob.name.lower():
            obs_to_delete.append(ob)
        
        
    if len(obs_to_delete)>0: #so blender doesnt complain about changing the structure while cycling
        print("we have {} object to delete".format(len(obs_to_delete)))
        for ob in obs_to_delete:
             bpy.data.objects.remove(ob)
        
def loadLdrawPart(fullpath_part,ldraw_full_directory,defaultColour):
    
    if not fullpath_part.endswith(".dat"):
         raise Exception("Not good fullpath_part:{}".format(fullpath_part))  
    
    #this is the high level function, its the same as clicking import, it use usersettings always (i.e cant change the color on the fly.)
    
    #bpy.ops.import_scene.lpub3dimportldraw(filepath=ldrawpart_fullpath, ldrawPath=ldraw_full_directory, modelFile=ldrawpart_fullpath) 
    loadldraw.Options.defaultColour=defaultColour
    loadldraw.loadFromFile(None,fullpath_part) # this is the "low level" function of the module 

def getCamera():
    camera_obj=None
    for ob in bpy.data.objects:
        if "camera" in ob.name.lower():
            camera_obj=ob
            break
    if camera_obj is None:
        raise Exception("No camera found")
    return camera_obj

def getCameraInfoFromScene():
    camera_obj=getCamera()
    print("CameraProp(({},{},{}),({},{},{}))".format(camera_obj.location.x,camera_obj.location.y,camera_obj.location.z,camera_obj.rotation_euler.x,camera_obj.rotation_euler.y,camera_obj.rotation_euler.z))
    #print("camera location:{}".format(camera_obj.location))
    #print("camera rotation:{}".format(camera_obj.rotation_euler))
        
def adjustCamera(camera_prop):
    #adjust camera
    camera_obj=getCamera()
    
    camera_obj.location = camera_prop.location
    #print(camera_obj.rotation_euler)
    camera_obj.rotation_euler = camera_prop.rotation

def adjustLight(light_prop):
    light_obj=None
    for ob in bpy.data.objects:
        if "light" in ob.name.lower():
            light_obj=ob
            break
    if light_obj is None:
        raise Exception("No light found")
    light_obj.location = light_prop.location
    light_obj.data.energy=light_prop.energy

def adjustGroundPlane(plane_prop):
    plane_obj=None
    for ob in bpy.data.objects:
        if "plane" in ob.name.lower():
            plane_obj=ob
            break
    if plane_obj is None:
        print("Mat_LegoGroundPlane not found, meaning this is the first import or the ground plane was deleted")
        return
    #bpy.data.materials["Mat_LegoGroundPlane"].node_tree.nodes["Diffuse BSDF"].inputs[0].default_value = (0.650006, 0.650006, 0.650006, 1) #simil grey
    bpy.data.materials["Mat_LegoGroundPlane"].node_tree.nodes["Diffuse BSDF"].inputs[0].default_value = plane_prop.diffuse_color
    plane_obj.location = plane_prop.location
    plane_obj.rotation_euler = plane_prop.rotation

def renderScene(fullpath_outputfile):
    active_scene = bpy.context.scene
    active_scene.render.resolution_x = 200
    active_scene.render.resolution_y = 200
    active_scene.render.engine = 'CYCLES'
    active_scene.render.image_settings.color_mode = 'RGBA'
    active_scene.render.film_transparent = True
    active_scene.render.image_settings.file_format = "PNG"
    active_scene.render.filepath = fullpath_outputfile
    active_scene.cycles.samples = 1024
    #bpy.ops.render.render('INVOKE_DEFAULT', write_still=True)
    bpy.ops.render.render(write_still=True)



def renderPart(partname,ldraw_full_directory,defaultColour,output_base_dir,camera_props,light_props,grounplane_props):
    if not os.path.exists(output_base_dir):
        raise Exception("output_dir:{} does not exist".format(output_base_dir))
    if not os.path.exists(ldraw_full_directory):
        raise Exception("ldraw_full_directory:{} does not exist".format(ldraw_full_directory))
    ldrawpart_fullpath=os.path.join(ldraw_full_directory,"parts/"+partname+".dat")
    if not os.path.exists(ldrawpart_fullpath):
        raise Exception("ldrawpart_fullpath:{} does not exist".format(ldrawpart_fullpath))
    output_dir=os.path.join(output_base_dir,partname)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print("Resetting the scene...")    
    resetScene()
    loadLdrawPart(ldrawpart_fullpath,ldraw_full_directory,defaultColour) #14 yellow, dealing with minifig head 
    
    i=1
    for groundplane_prop in grounplane_props:
        for light_prop in light_props:
            for camera_prop in camera_props:
                print("Rendering pos:{} for part:{}".format(i,partname))  
                fullpath_outputfile=os.path.join(output_dir,"{}-{}.png".format(partname,i))
                adjustCamera(camera_prop)
                adjustLight(light_prop)
                adjustGroundPlane(groundplane_prop)
                renderScene(fullpath_outputfile)
                i+=1
                print("Done rendering {}...".format(i))
        
    
    print("Part:{} Done. Output dir:{}".format(partname,output_dir))
    
print("Setting GPU for rendering...")
bpy.context.scene.cycles.device = 'GPU'


#ldrawpart_fullpath="C:\\Users\\Alessio\\Documents\\ProgettieLavoro\\lavoro_personale\\legoNew\\ldraw\\parts\\3626bp8k.dat"
ldraw_full_directory="C:\\Users\\Alessio\\Documents\\ProgettieLavoro\\lavoro_personale\\legoNew\\ldraw\\"
render_base_directory="C:\\Users\\Alessio\\Documents\\ProgettieLavoro\\lavoro_personale\\legoNew\\render\\"

#1.5708 is 90 degrees in radians

#adjustGroundPlane()
#getCameraInfoFromScene()
#adjustCamera(CameraProp((0, -0.45, -0.2),(1.5, 0, 0)))

#fullpath_outputfile=render_base_directory+ldrawpart_fullpath.split("\\")[-1].replace(".dat",".png")
#renderScene(fullpath_outputfile)

#


#loadldraw.loadFromFile(None,ldrawpart_fullpath)

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
    
light_props=[LightProp((0.2,-4,2),30),
                 LightProp((0.2,-4,2),60),
                 LightProp((-0.3,-4,3),30),
                 LightProp((-0.3,-4,3),60),
                 LightProp((0.2,-4,-2),30),
                 LightProp((0.2,-4,-2),60),
                 LightProp((-0.3,-4,-3),30),
                 LightProp((-0.3,-4,-3),60)]

plane_props=[PlaneProp((0.0,1.3,0.0),(1.5708,0.0,0.0),(0.650006, 0.650006, 0.650006, 1)), #light grey
             PlaneProp((0.0,1.3,0.0),(1.5708,0.0,0.0),(0.0, 0.0, 0.0, 1))] #black   

renderPart("3626bp8k",ldraw_full_directory,"14",render_base_directory,camera_props,light_props,plane_props)
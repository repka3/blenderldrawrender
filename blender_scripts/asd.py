import bpy

print("Setting GPU for rendering...")
bpy.context.scene.cycles.device = 'GPU'

print("Creating new blank scene...")
#bpy.ops.wm.read_factory_settings(use_empty=True)

ldrawpart_fullpath="C:\\Users\\Alessio\\Documents\\ProgettieLavoro\\lavoro_personale\\legoNew\\ldraw\\parts\\3626bph3.dat"
ldraw_full_directory="C:\\Users\\Alessio\\Documents\\ProgettieLavoro\\lavoro_personale\\legoNew\\ldraw\\"

from io_scene_lpub3d_importldraw.loadldraw import loadldraw

loadldraw.Options.defaultColour="10"

bpy.ops.import_scene.lpub3dimportldraw(filepath=ldrawpart_fullpath, ldrawPath=ldraw_full_directory, modelFile=ldrawpart_fullpath)


#loadldraw.loadFromFile(None,ldrawpart_fullpath)

import bpy
import os
import math
#import random
output_directory = "/path/directory"
num_cameras = 8
camera_distance = 5.0
camera_height = 2.0
render_samples = 128 
resolution_x = 1024 # Square images
resolution_y = 1024


# Render Settings:
def setup_render_settings():
    scene = bpy.context.scene #Gets the active scene
    scene.render.engine = 'CYCLES' #Encourages better lighting for plastic objects
    scene.render.image_settings.color_mode = 'RGBA' # Colour profile with transparency
    scene.render.image_settings.file_format = 'PNG' # Render to a .png file
    scene.render.film_transparent = True # Keep the .png background clear
    
    scene.render.resolution_x = resolution_x
    scene.render.resolution_y = resolution_y
    
    scene.cycles.device = 'GPU' # Use the GPU
    scene.cycles.samples = render_samples

#Create the cameras:
def create_camera_rig(target_object):
    cameras = []
    for i in range (num_cameras):
        angle = i * (2 * math.pi / num_cameras)
        x = camera_distance *math.cos(angle)
        y = camera_distance * math.sin(angle)
        z = camera_height
        bpy.ops.object.camera_add(location=(x ,y,z))
        cam = bpy.context.active_object
        cam.name = f"RenderCam_{i}"
        
        constraint = cam.constraints.new(type='TRACK_TO')
        constraint.target = target_object
        constraint.track_axis = 'TRACK_NEGATIVE_Z'
        constraint.up_axis = 'UP_Y'
        
        cameras.append(cam)
    return cameras

# Action to render the different views
def render_all_views(cameras, object_name):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        
    scene = bpy.context.scene
    
    for i, cam in enumerate (cameras):
        print(f"Rendering camera {i}")
        scene.camera = cam
        
        filename = f"{object_name}_{i}.png"
        scene.render.filepath = os.path.join(output_directory, filename)
        bpy.ops.render.render(write_still=True)


target = bpy.context.active_object #Targets the selected object

if target and target.type == 'MESH':
    obj_name = target.name
    safer_name =obj_name.replace(".", "_").replace(" ", "_")
    print (f"Processing and also prnt test name is saving properly: {safer_name}")
    setup_render_settings()
    cams = create_camera_rig(target)
    render_all_views(cams, safer_name) #use the render settings on the cameras we created
    print(f"Saved as {safer_name}_#.png to: {output_directory}")
else:
    print(f"Not saved, try selecting the object")
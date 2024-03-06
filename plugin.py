import bpy  # Import the Blender Python module
import math  # Import the math module for mathematical operations

# Function to add an image plane to the scene
def add_image_plane(image_path, location=(0, 0, 0), scale=(1, 1, 1)):
    # Use Blender's built-in operator to import an image as a plane
    bpy.ops.import_image.to_plane(files=[{"name": image_path}], directory=r"C:\Users\Shayne\Desktop\TD Final Project\C01020_Env.png")
    # Get a reference to the newly created plane object
    plane = bpy.context.object
    #Set the location of the plane in 3D space
    plane.location = location
   # Set the scale of the plane
    plane.scale = scale

# Function to create a lightbox in the scene
def create_lightbox(location=(0, 0, 0), size=1):
    # Use Blender's built-in operator to add a plane mesh
    bpy.ops.mesh.primitive_plane_add(size=size, location=location)
    # Get a reference to the newly created plane object
    plane = bpy.context.object
    # Rotate the plane 90 degrees along the Z-axis
    plane.rotation_euler = (0, 0, math.radians(90))
    # Use Blender's built-in operator to add a sunlight
    bpy.ops.object.light_add(type='SUN', location=location)
    # Get a reference to the newly created sunlight object
    sun_light = bpy.context.object
    # Set the energy of the sunlight to 1000
    sun_light.data.energy = 1000

# Function to create preset cameras in the scene
def create_preset_cameras():
    # Define parameters for preset cameras
    camera_params = [
        {"name": "Camera_1", "location": (-10, -30, 0), "rotation": (math.radians(90),math.radians(0),math.radians(-20))},
        {"name": "Camera_2", "location": (0, -50, 0), "rotation": (math.radians(90),math.radians(0),math.radians(0))},
        {"name": "Camera_3", "location": (10, -10, 0), "rotation": (math.radians(90),math.radians(0),math.radians(20))}
    ]

    # Loop through each camera parameter
    for params in camera_params:
        
        # Create a new camera data object
        camera_data = bpy.data.cameras.new(name=params["name"])
        # Set the lens of the camera to 50mm
        camera_data.lens = 50
        # Set the sensor width and height of the camera
        camera_data.sensor_width = 18.96
        camera_data.sensor_height = 10
        # Create a new camera object with the camera data
        camera = bpy.data.objects.new(params["name"], camera_data)
        # Set the location and rotation of the camera
        camera.location = params["location"]
        camera.rotation_euler = params["rotation"]
        # Link the camera object to the scene collection
        bpy.context.scene.collection.objects.link(camera)

# Entry point of the script
if __name__ == "__main__":
    # Specify the path to the image file
    image_path = r"C:\Users\User\Desktop\TD Final Project\C01020_Env.png"
    # Specify the location of the lightbox
    lightbox_location = (10, -6, 4)
    # Specify the size of the lightbox
    lightbox_size = 11.0

    # Call the functions to add an image plane, create a lightbox, and create preset cameras
    add_image_plane(image_path)
    create_lightbox(lightbox_location, lightbox_size)
    create_preset_cameras()

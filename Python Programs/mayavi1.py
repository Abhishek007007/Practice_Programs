from mayavi import mlab

# To access any VTK object, we use 'tvtk', which is a Python wrapping of
# VTK replacing C++ setters and getters by Python properties and
# converting numpy arrays to VTK arrays when setting data.
from tvtk.api import tvtk
from tvtk.common import configure_input_data

v = mlab.figure()

# Create a sphere
# The source generates data points
sphere = tvtk.SphereSource(center=(0, 0, 0), radius=0.5)
# The mapper converts them into position in, 3D with optionally color (if
# scalar information is available).
sphere_mapper = tvtk.PolyDataMapper()
configure_input_data(sphere_mapper, sphere.output)
sphere.update()

# The Property will give the parameters of the material.
p = tvtk.Property(opacity=0.2, color=(1, 0, 0))
# The actor is the actually object in the scene.
sphere_actor = tvtk.Actor(position=(0, 0, 0), mapper=sphere_mapper, property=p)
v.scene.add_actor(sphere_actor)

# Create a cylinder
cylinder = tvtk.CylinderSource(center=(0, 0, 0), radius=0.2, resolution=16)
cylinder_mapper = tvtk.PolyDataMapper()
configure_input_data(cylinder_mapper, cylinder.output)
cylinder.update()
p = tvtk.Property(opacity=0.3, color=(0, 0, 1))
cylinder_actor = tvtk.Actor(position=(7, 0, 1), mapper=cylinder_mapper,
                            property=p, orientation=(90, 0, 90))
v.scene.add_actor(cylinder_actor)

# Create a line between the two spheres
line = tvtk.LineSource(point1=(0, 0, 0), point2=(7, 0, 1))
line_mapper = tvtk.PolyDataMapper()
configure_input_data(line_mapper, line.output)
line.update()
line_actor = tvtk.Actor(mapper=line_mapper)
v.scene.add_actor(line_actor)

# And display text
vtext = tvtk.VectorText()
vtext.text = 'Vettu'
text_mapper = tvtk.PolyDataMapper()
configure_input_data(text_mapper, vtext.get_output())
vtext.update()
p2 = tvtk.Property(color=(0, 0.3, 0.3))
text_actor = tvtk.Follower(mapper=text_mapper, property=p2)
text_actor.position = (0, 0, 0)
v.scene.add_actor(text_actor)

# Choose a view angle, and display the figure
mlab.view(85, -17, 15, [3.5, -0.3, -0.8])
mlab.show()
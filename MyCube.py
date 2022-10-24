from sightpy import *

# define materials to use

floor = Glossy(diff_color = image("checkered_floor.png", repeat = 2.),  roughness = 0.2, spec_coeff = 0.3, diff_coeff = 0.7, n = vec3(2.2, 2.2, 2.2)) # n = index of refraction
blue_glass = Refractive(n = vec3(1.5 + 4e-8j,1.5 +  4e-8j,1.5 +  0.j)) # Para el cuboide
red_glass = Refractive(n = vec3(1.5 + 0.j,1.5 +  5e-8j,1.5 +  5e-8j)) # Para la esfera roja de vidrio
bluish_metal = Glossy(diff_color = rgb(0.0, 0, 0.1), n = vec3(1.3+1.91j, 1.3+1.91j, 1.4+2.91j), roughness = 0.2,spec_coeff = 0.5, diff_coeff= 0.3) # Para la esfera de metal



# Set Scene 

Sc = Scene()
Sc.add_Camera(look_from = vec3(0., 0.25, 1. ), look_at = vec3(0., 0.25, -3.),
	          screen_width = 1920 , # para resolución 4K (1920x1080)
	          screen_height = 1080)


Sc.add_DirectionalLight(Ldir = vec3(0.0,0.5, 0.5),  color = rgb(0.5, 0.5, 0.5))

Sc.add(Plane(material = floor,  center = vec3(0, -0.5, -3.0), width = 6.0,height = 6.0, u_axis = vec3(1.0, 0, 0), v_axis = vec3(0, 0, -1.0) , max_ray_depth = 5))

# Creamos los objetos de las diferentes clases (1 cubo de la case 'Cuboid', 2 esferas de la clase 'Sphere') #180,1.2,0.25
gcb_c = Cuboid( material = blue_glass, center = vec3(-0.8, 0.5, -0.8), width = 0.9,height = 1.0, length = 0.4, shadow = False,  max_ray_depth = 5)
bm_s = Sphere(material = bluish_metal, center = vec3(-1.1, 0.27, -4), radius = .25, shadow = False,max_ray_depth = 3)
rc_s = Sphere(material = red_glass, center = vec3(1, 0.25, -1), radius = .26, shadow = False,max_ray_depth = 3)

# Aplicamos la rotación al cuboide azul de cristal 
gcb_c.rotate(θ = 91, u = vec3(0,1,0))

# Agregamos nuestros objetos a la escena
Sc.add(gcb_c)
Sc.add(bm_s)
Sc.add(rc_s)


#see sightpy/backgrounds
Sc.add_Background("stormydays.png")

# Render 
img = Sc.render(samples_per_pixel = 4)

img.save("EXAMPLE3_90.png")

img.show()
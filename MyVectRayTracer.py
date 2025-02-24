from sightpy import * # Utilizamos todos los elementos de la carpeta 'sightpy'

def main():
    # DEF Materiales de las figuras: refractive -> cristal; glossy -> solido ====================================================

    floor = Glossy(diff_color = image("checkered_floor.png", repeat = 2.),  roughness = 0.2, spec_coeff = 0.3, diff_coeff = 0.7, n = vec3(2.2, 2.2, 2.2)) # n = index of refraction
    blue_glass = Refractive(n = vec3(1.5 + 4e-8j,1.5 +  4e-8j,1.5 +  0.j)) # Para el cuboide
    red_glass = Refractive(n = vec3(1.5 + 0.j,1.5 +  5e-8j,1.5 +  5e-8j)) # Para la esfera roja de vidrio
    bluish_metal = Glossy(diff_color = rgb(0.0, 0, 0.1), n = vec3(1.3+1.91j, 1.3+1.91j, 1.4+2.91j), roughness = 0.2,spec_coeff = 0.5, diff_coeff= 0.3) # Para la esfera de metal

    # CONF Escena ===============================================================================================================
    # para resolución 4K (1920x1080)
    Sc = Scene() # Creamos objeto de la clase 'Scene'
    Sc.add_Camera(look_from = vec3(0., 0.25, 1. ), look_at = vec3(0., 0.25, -3.),
                screen_width = 1920 , 
                screen_height = 1080)

    Sc.add_DirectionalLight(Ldir = vec3(0.0,0.5, 0.5),  color = rgb(0.5, 0.5, 0.5))
    Sc.add(Plane(material = floor,  center = vec3(0, -0.5, -3.0), width = 6.0,height = 6.0, u_axis = vec3(1.0, 0, 0), v_axis = vec3(0, 0, -1.0) , max_ray_depth = 5))

    # CREAR Objetos de las clases (para las figuras) ===========================================================================
    # Creamos los objetos de las diferentes clases (1 cubo de la case 'Cuboid', 2 esferas de la clase 'Sphere') #180,1.2,0.25
    gcb_c = Cuboid( material = blue_glass, center = vec3(-0.8, 0.5, -0.8), width = 0.9,height = 1.0, length = 0.4, shadow = False,  max_ray_depth = 5)
    bm_s = Sphere(material = bluish_metal, center = vec3(-1.1, 0.27, -4), radius = .25, shadow = False,max_ray_depth = 3)
    rc_s = Sphere(material = red_glass, center = vec3(1, 0.25, -1), radius = .26, shadow = False,max_ray_depth = 3)

    """
    Mi código para matrices vectorizadas: https://colab.research.google.com/drive/13HJRpq5yvdYZ7UjErlCIFdDi4RRdRd-H?hl=es
    """
    # Aplicamos la rotación al cuboide azul de cristal 
    gcb_c.rotate(θ = 91, u = vec3(0,1,0)) #Utilizando la función 'rotate()' de la clase 'Cuboid'

    # ADD Agregamos nuestros objetos a la escena
    Sc.add(gcb_c)
    Sc.add(bm_s)
    Sc.add(rc_s)

    # Agregamos el fondo a la escena 
    Sc.add_Background("stormydays.png")

    # Renderizamos
    img = Sc.render(samples_per_pixel = 4)
    img.save("EXAMPLE3_90.png") # Vamos cambiando el nombre: "EXAMPLE_"+str(i)+".png"
    img.show() #Vemos la imagen

    # Usamos el archivo 'MyGIF.py' para generar un GIF a partir de los frames obtenidos.

if __name__=="__main__":
    main()

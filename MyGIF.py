import glob
from PIL import Image
def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frame_one = frames[0]
    frame_one.save("RayTracerSPC.gif", format="GIF", append_images=frames,
               save_all=True, duration=33.3, loop=0) #duration en ms, loop = 0 -> infty
    
def main():
    frame_folder = r"D:\PROGRAMMING\GitHub\SAtec\Python-Raytracer\frames"
    make_gif(frame_folder)

if __name__ == "__main__":
    make_gif(r"D:\PROGRAMMING\GitHub\SAtec\Python-Raytracer\frames")

#https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/
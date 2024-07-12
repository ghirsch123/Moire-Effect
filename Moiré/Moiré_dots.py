import numpy as np
from PIL import Image, ImageDraw
import imageio

def generate_frame(size, dots, shift):
    # generating a frame of the Moiré pattern
    image = Image.new("L", (size,size), 255)
    draw = ImageDraw.Draw(image)

    for i in range(dots):
        for j in range(dots): # looping through all dots
            x = int(i * size / dots + shift * i) # calculates x position of dot
            y = int(j * size / dots + shift * j) # calculates y position of dot
            draw.ellipse((x, y, x + 5, y + 5), fill=0) # draw a circle at said position
    return np.array(image) # imageio expects input frames to be in the form of numpy arrays

def create_moire_gif(filename, size=500, dots=20, frames=30):
    # creating a compiled gif
    images = []
    for shift in np.linspace(0,5, frames): # loops through a sequence of shift values
        frame = generate_frame(size, dots, shift)
        images.append(frame)
    imageio.mimsave(filename, images, duration = 0.1)

create_moire_gif("moire.gif")
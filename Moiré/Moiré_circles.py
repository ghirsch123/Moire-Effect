import numpy as np
from PIL import Image, ImageDraw
import imageio

def generate_frame(size, circles, shift):
    # goal is to generate a single frame with two overlapping concentric circles
    image = Image.new("L", (size, size), 255) # basics to just draw an image
    draw = ImageDraw.Draw(image)

    center_x = size // 2
    center_y = size // 2 # center of the image

    for i in range(1, circles + 1):
        radius = i * size // (2 * circles) # radius of each circle gets smaller depending on how many there are
        draw.ellipse((center_x - radius - shift, center_y - radius, center_x + radius - shift, center_y + radius), outline=0, width = 3) # slides left

    # repeat for the second layer of circles, but shifted slightly
    for i in range(1, circles + 1):
        radius = i * size // (2 * circles) # radius of each circle gets smaller depending on how many there are
        draw.ellipse((center_x - radius + shift, center_y - radius, center_x + radius + shift, center_y + radius), outline=0, width = 3) # slides right

    return np.array(image)

def create_moire_gif(filename, size=500, circles=20, frames=60):
    images = []
    max_shift = size // (2 * circles)
    for shift in np.linspace(0, max_shift, frames):
        frame = generate_frame(size, circles, shift)
        images.append(frame)
    imageio.mimsave(filename, images, duration=0.1)

create_moire_gif("moire_circles.gif")
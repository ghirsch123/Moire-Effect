import numpy as np
from PIL import Image, ImageDraw
import imageio

def generate_frame(size, dots, shift):
    # generating a frame of the Moiré pattern
    image = Image.new("L", (size,size), 255)
    draw = ImageDraw.Draw(image)

    spacing = size // dots

    for i in range(dots):
        for j in range(dots):
            x = i * spacing + shift[i, j, 0]
            y = i * spacing + shift[i, j, 1]
            draw.ellipse((x, y, x + 5, y + 5), fill=0)
    return np.array(image)

def create_random_moire_gif(filename, size=500, dots=20, frames=30):
    images = []
    shifts = np.zeros((dots, dots, 2))
    max_shift = size // (4 * dots)
    
    for _ in range(frames):
        shifts += np.random.uniform(-max_shift, max_shift, (dots, dots, 2))
        frame = generate_frame(size, dots, shifts)
        images.append(frame)
    
    imageio.mimsave(filename, images, duration=0.1)

# Create the GIF
create_random_moire_gif("random_moire.gif")


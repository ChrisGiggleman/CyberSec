import imageio.v3 as iio
from PIL import Image
import numpy as np

# List your images
filenames = ["batdog.png.jpg", "batdog2.png.jpg"]

images = []
for fname in filenames:
    img = Image.open(fname).convert("RGBA")   # ensure RGBA
    images.append(np.array(img))

# Save as GIF
iio.imwrite("team.gif", images, duration=500, loop=0)



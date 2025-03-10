import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = [
    "codedex/nyan-cat1.png", 
    "codedex/nyan-cat2.png", 
    "codedex/nyan-cat3.png"
]

images = []

target_image = Image.open(filenames[0])
target_size = target_image.size

for filename in filenames:
    img = Image.open(filename).convert("RGB")
    img_resized = img.resize(target_size, Image.LANCZOS)
    images.append(np.array(img_resized))

# Ensure all images have the same shape
image_shapes = [img.shape for img in images]
if len(set(image_shapes)) != 1:
    raise ValueError("Not all images have the same shape")

iio.imwrite("cat.gif", images, duration=500, loop=0)

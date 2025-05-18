from PIL import Image
import numpy as np

img = Image.open("challenge.png")
pixels = np.array(img)

width = 400 
height = 100
reshaped = pixels.reshape((height, width, 3))  
Image.fromarray(reshaped).save(f"flag.png")

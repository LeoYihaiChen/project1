from PIL import Image as IM
import numpy as nu
from colors import colorslist

HEIGHT = 300
WIDTH = 300

# empty list
pixels = []

for j in range(HEIGHT):
    pixel_line = [colorslist["black"]] * WIDTH

    for i in range(WIDTH):
        color = None
        
        if i < WIDTH / 3:
            if j < HEIGHT / 3:
                color = "red"
            elif j < HEIGHT / 3 * 2:
                color = "orange"
            else:
                color = "yellow"
        elif i < WIDTH / 3 * 2:
            if j < HEIGHT / 3:
                color = "green"
            elif j < HEIGHT / 3 * 2:
                color = "cyan"
            else:
                color = "blue"
        else:
            if j < HEIGHT / 3:
                color = "purple"
            elif j < HEIGHT / 3 * 2:
                color = "pink"
            else:
                color = "brown"
                
        pixel_line[i] = colorslist[color]
        
    pixels.append(pixel_line)

pixel_array = nu.array(pixels, dtype=nu.uint8)
img = IM.fromarray(pixel_array, mode="RGB")   
img.save('/Users/yihaichen/Desktop/mycomputer/code/code/python/windowpy/images/3x3_image.bmp')

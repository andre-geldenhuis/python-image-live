from pathlib import Path
from PIL import Image, ImageDraw

def imageprocess(filepath):

        output_path = 'output'
        print(filepath)
        im = Image.open(filepath)

        #Store the width and height
        width, height = im.size

        # Setting the points for cropped image
        left = 0
        top = 0
        right = width
        bottom = height-100      

        #crop the bottom off the image
        im_cropped = im.crop((left, top, right, bottom))
        
        #Prepare rectangle
        draw = ImageDraw.Draw(im_cropped)

        #get new image width and height, this'll make the math easier
        width, height = im_cropped.size

        #Size of rectangle
        w, h = 200, 100

        #coordinates of the rectangle
        x0 = 0
        y0 = height - h
        x1 = w
        y1 = height

        shape = [(x0, y0), (x1, y1)]
        draw.rectangle(shape, fill ="black",outline ="black")

        outpath = Path.cwd().joinpath(output_path,filepath.name)
        im_cropped.save(outpath)
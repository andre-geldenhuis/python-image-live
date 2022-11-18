from pathlib import Path
from PIL import Image, ImageDraw
from library.imagefunctions import imageprocess #note change!

test_path = 'test_data'
output_path = 'output'

#Set raw path to test data for now
raw_path = test_path

# Generate Path objects
raw_path = Path.cwd().joinpath(test_path,'images')
imfiles = raw_path.glob("*.JPG")

# Print filepath we're working on and process filepath
for filepath in imfiles:
    imageprocess(filepath)

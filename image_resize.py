from PIL import Image
from os import listdir, getcwd
from os.path import isfile, join
import re
import sys
import math

print(sys.argv)

def linkrepl(matchobj):
    """replace img_title with img_title_resized"""
    file_name = matchobj.group(0)
    return file_name + "_resized"

percentage = int(sys.argv[1]) if len(sys.argv) > 1 else 50

print(percentage)

if not isinstance(percentage, (int, float, complex)):
    raise TypeError("Argument must be a percentage number, argument was " + percentage)

# resize dimensions
resize_dimensions = {
    'phone': {
        'v': (907, 1209),
        'h': (1613, 1210)
    },
    'film': {
        'v': (),
        'h':(1252, 830)
    }
}
film_photo_h = (1252, 830)
phone_photo_v = (907, 1209)
film_photo_v = ()
phone_photo_h = (1613, 1210)

# list all images in the folder
current_dir = getcwd()
print(current_dir)
for f in listdir(current_dir):
    print(f)
onlyimagefiles = [f for f in listdir(current_dir) if isfile(join(current_dir, f)) and bool(re.search(r"\.(gif|jpe?g|tiff?|png|webp|bmp)", f))]

print(onlyimagefiles)

for image_file in onlyimagefiles:
    image = Image.open(image_file)

    new_height = math.floor(image.height * (percentage/100))
    new_width = math.floor(image.width * (percentage/100))

    new_image = image.resize((new_width, new_height))

    link_regex = re.compile(
        r"[^\.]+"
    )  # match anything in the description in format [words words]
    new_filename = link_regex.sub(linkrepl, image_file, 1)
    print(new_filename)
    new_image.save(new_filename)

# loop through and resize them all

# two different resizings - one for horizontal, one for vertical

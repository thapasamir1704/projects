import sys
import os
from PIL import Image

initialfolder = sys.argv[1]
destinationfolder = sys.argv[2]

if not os.path.exists(destinationfolder):
    os.makedirs(destinationfolder)

for filename in os.listdir(initialfolder):
  new_name = os.path.splitext(filename)[0]
  img = Image.open(f"{initialfolder}\\{filename}")
  img.save(f'{destinationfolder}\\{new_name}.png', 'png')
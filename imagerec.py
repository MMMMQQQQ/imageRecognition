from PIL import Image
import numpy as np

i=Image.open('tutorialimages/images/dot.png')
iar=np.asarray(i)

print(iar)
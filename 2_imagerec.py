from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i=Image.open('tutorialimages/images/dotndot.png')
iar=np.asarray(i)

# imshow:show the image
plt.imshow(iar)
plt.show()
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i=Image.open('tutorialimages/images/numbers/y0.4.png')
iar=np.asarray(i)

# imshow:show the image
plt.imshow(iar)
print(iar)
plt.show()
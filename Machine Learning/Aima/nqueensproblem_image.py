from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
im = Image.open('images/queen.png')
height = im.size[1]
im = np.array(im).astype(np.float) / 255
fig = plt.figure()
plt.plot(np.arange(10), 4 * np.arange(10))
fig.figimage(im, 0, fig.bbox.ymax - height)
plt.show()
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
#
# # wczytywanie obrazów
# img = mpimg.imread('user_photo.jpg')
#
# plt.imshow(img)
# plt.axis('off')
# plt.show()

from PIL import Image

image = Image.open('user_photo.jpg')
image.show()

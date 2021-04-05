from PIL import Image
from resizeimage import resizeimage

fd_img = open('test-image.jpeg', 'r')
img = Image.open(fd_img)
img = resizeimage.resize_height(img, 200)
img.save('test-image-height.jpeg', img.format)
fd_img.close()

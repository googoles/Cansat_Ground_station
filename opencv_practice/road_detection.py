import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
# reading in an image
image = mpimg.imread('services.jpeg')
# printing out some stats and plotting the image
print('This image is:', type(image), 'with dimensions:', image.shape)
# plt.imshow(image)
# plt.show()

def grayscale(image):

    return cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

def canny(img,low_threshold,high_threshold):
    return cv2.Canny(img, low_threshold,high_threshold)

low_threshold = 50
high_threshold = 200
edges = canny(image,low_threshold,high_threshold)



# gray = grayscale(image)
plt.figure(figsize=(10,8))
plt.imshow(edges, cmap='gray')
plt.show()


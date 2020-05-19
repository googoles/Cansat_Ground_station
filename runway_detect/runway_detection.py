import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
# reading in an image
image = mpimg.imread('runway_2.jpeg')
# printing out some stats and plotting the image
print('This image is:', type(image), 'with dimensions:', image.shape)
# plt.imshow(image)
# plt.show()

def grayscale(image):

    return cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

def gaussian_blur(image,kernel_size):
    return cv2.GaussianBlur(image,(kernel_size,kernel_size),0)

gray = grayscale(image)
kernel_size = 5
blur_gray = gaussian_blur(gray,kernel_size)

def canny(img,low_threshold,high_threshold):
    return cv2.Canny(img, low_threshold,high_threshold)

low_threshold = 50
high_threshold = 200
edges = canny(blur_gray,low_threshold,high_threshold)


plt.figure(figsize=(10,8))
plt.imshow(edges, cmap='gray')
plt.show()
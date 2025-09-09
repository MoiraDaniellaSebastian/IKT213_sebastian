import cv2
import numpy as np
def copy(image, emptyPictureArray):
    height,width,channels = image.shape

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                emptyPictureArray[i,j,k] = image[i,j,k]

    cv2.imwrite('copied_image.jpg', emptyPictureArray)
    print("Image saved as 'copied_image.jpg'")

if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Image does not exist")

    else:
        height,width, channels = image.shape
        emptyPictureArray = np.zeros((height, width, 3),dtype=np.uint8)
        copy(image, emptyPictureArray)

import cv2
import numpy as np


def hue_shifted(image, emptyPictureArray, hue):
    height, width, channels = image.shape

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                new_value = int(image[i, j, k]) + hue
                if new_value > 255:
                    emptyPictureArray[i, j, k] = 255
                elif new_value < 0:
                    emptyPictureArray[i, j, k] = 0
                else:
                    emptyPictureArray[i, j, k] = new_value

    cv2.imwrite('hue_shifted_image.jpg', emptyPictureArray)
    print("Image saved as 'hue_shifted_image.jpg'.")


if __name__ == "__main__":
    image = cv2.imread('lena.png')
    if image is None:
        print("Image does not exist.")
    else:
        height, width, channels = image.shape
        emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
        hue_shifted(image, emptyPictureArray, 50)
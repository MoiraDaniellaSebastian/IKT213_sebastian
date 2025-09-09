import cv2

def smoothing(image):
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imwrite('smoothed_image.jpg', blurred_image)
    print("Image saved as 'smoothed_image.jpg'.")

if __name__ == "__main__":
    image = cv2.imread('lena.png')
    if image is None:
        print("Image does not exist.")
    else:
        smoothing(image)
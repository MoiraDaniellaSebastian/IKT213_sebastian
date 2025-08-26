import cv2
def print_image_information(image):
    # get image dimensions
    height, width, channels = image.shape

    # image information
    print("height:", height)
    print("width:", width)
    print("channels:", channels)
    print("size:", image.size)
    print("data type:", image.dtype)

image = cv2.imread("lena-1.png")
print_image_information(image)
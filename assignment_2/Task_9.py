import cv2

def rotation(image, rotation_angle):
    if rotation_angle == 90:
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_angle == 180:
        rotated_image = cv2.rotate(image, cv2.ROTATE_180)
    else:
        print("Angle not supported. Please use 90 or 180 degrees. ")
        rotated_image = image

    cv2.imwrite('rotated_image.jpg', rotated_image)
    print("Image saved as 'rotated_image.jpg'.")


if __name__ == "__main__":
    image = cv2.imread('lena.png')
    if image is None:
        print("Image does not exist.")
    else:
        rotation(image, 180)
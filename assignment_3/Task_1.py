import cv2
import numpy as np


def sobel_edge_detection(image):

    # Convert to graycsale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

    # Sobel Edge Detection
    sobel_edges =(255*cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=1) ).clip(0,255).astype(np.uint8)  # Combined X and Y Sobel Edge Detection
    cv2.imwrite("sobel_detection.png",sobel_edges )

def canny_edge_detection (image, threshold_1, threshold_2):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

    cannyEdges = cv2.Canny(img_blur, threshold_1, threshold_2)
    cv2.imwrite("canny_detection.png" , cannyEdges)

def template_match(image, template):

    img_color = cv2.imread(image)
    if img_color is None:
        raise FileNotFoundError(f"Image not found: {image}")

    # Make grayscale copy for matching
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # Read template in GRAY
    tmpl = cv2.imread(template, 0)
    if tmpl is None:
        raise FileNotFoundError(f"Template not found: {template}")

    h, w = tmpl.shape[:2]

    # Perform template matching
    res = cv2.matchTemplate(img_gray, tmpl, cv2.TM_CCOEFF_NORMED)
    ys, xs = np.where(res >= 0.9)

    # Draw red rectangles on the COLOR image
    for x, y in zip(xs, ys):
        cv2.rectangle(img_color, (x, y), (x+w, y+h), (0,0,255), 2)

    cv2.imwrite("shapes_matches.png", img_color)

def resize(image, scale_factor: int, up_or_down: str):
    if  up_or_down.lower() == "up":
       resized_image = cv2.pyrUp(image)
       print(f"Image upsampled by factor of {scale_factor}")
       cv2.imwrite("resized_image_up.png", resized_image)

    elif up_or_down.lower() == "down":
        resized_image = cv2.pyrDown(image)
        print(f"Image upsampled by factor of {scale_factor}")
        cv2.imwrite("resized_image_down.png", resized_image)

    return resized_image


# Read the original image
img = cv2.imread('lambo.png')
sobel_edge_detection(img)
canny_edge_detection(img, 50, 50)
template_match("shapes-1.png", "shapes_template.jpg")
resize(img, 2, "up")
resize(img, 2, "down")




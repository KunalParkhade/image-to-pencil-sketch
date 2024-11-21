import cv2
import numpy as np

def convert_to_grayscale(image_np):
    """
    Converts an image from RGB to grayscale.
    """
    return cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

def create_pencil_sketch(image_np, blur_intensity=21, detail_level=256):
    """
    Takes an RGB image and creates a pencil sketch.
    """
    # Image to grayscale
    gray_image = convert_to_grayscale(image_np)

    # Invert the grayscale image
    inverted_image = 255 - gray_image

    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(inverted_image, (blur_intensity, blur_intensity), sigmaX=0, sigmaY=0)

    # Invert the blurred image
    inverted_blur = 255 - blurred_image

    # CReating pencil sketch by blending the grayscale and inverted blurred image
    sketch = cv2.divide(gray_image, inverted_blur, scale=detail_level)

    return sketch

import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(file_path):
    # Load and return the original image
    image = cv2.imread(file_path)
    return image

def convert_to_grayscale(image):
    # Convert image to grayscale
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_gaussian_blur(image):
    # Apply Gaussian Blur to reduce noise
    return cv2.GaussianBlur(image, (5, 5), 0)

def detect_edges(image):
    # Detect edges using Canny Edge Detection
    return cv2.Canny(image, 50, 150)

def define_region_of_interest(image):
    # Define a polygon mask for the lane area
    height, width = image.shape
    mask = np.zeros_like(image)

    # Define a triangular region for the lane area
    polygon = np.array([[
        (0, height),
        (width, height),
        (width // 2, height // 2)
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def detect_lines(image):
    # Use Hough Transform to detect lines
    return cv2.HoughLinesP(
        image,
        rho=1,
        theta=np.pi / 180,
        threshold=50,
        minLineLength=100,
        maxLineGap=50
    )

def draw_lines(image, lines):
    # Draw lines on the image
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    combined_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)
    return combined_image

def lane_detection_pipeline(file_path):
    # Lane detection pipeline function
    image = load_image(file_path)
    gray = convert_to_grayscale(image)
    blur = apply_gaussian_blur(gray)
    edges = detect_edges(blur)
    roi = define_region_of_interest(edges)
    lines = detect_lines(roi)
    lane_image = draw_lines(image, lines)
    
    # Show results
    plt.figure(figsize=(10, 8))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(lane_image, cv2.COLOR_BGR2RGB))
    plt.title("Lane Detection")
    plt.axis("off")
    
    plt.show()

# Run the pipeline with the sample image
lane_detection_pipeline('road_sample.jpg')

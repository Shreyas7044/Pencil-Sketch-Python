import cv2

# Read image
image = cv2.imread("input.jpg")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert image
inverted_image = 255 - gray_image

# Blur image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# Invert blurred image
inverted_blur = 255 - blurred

# Create pencil sketch
pencil_sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

# Show result
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)

# Save result (optional)
cv2.imwrite("sketch.png", pencil_sketch)
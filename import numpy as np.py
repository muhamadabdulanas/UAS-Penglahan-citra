import numpy as np
import matplotlib.pyplot as plt
import cv2

# Path to your image
image_path = 'd:\\4.jpeg'

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise ValueError(f"Image not found or unable to load: {image_path}")

# Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(image_rgb)
plt.title('Loaded Image')
plt.axis('off')
plt.show()


# Reshape the image to a 2D array of pixels and 3 color values (RGB)
pixel_vals = image.reshape((-1, 3))

# Convert to float type
pixel_vals = np.float32(pixel_vals)

# Define criteria for K-means algorithm
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)

# Number of clusters (K)
k = 3

# Apply K-means clustering
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert data back to 8-bit values
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]

# Reshape data to the original image dimensions
segmented_image = segmented_data.reshape((image.shape))

# Display the segmented image
plt.imshow(segmented_image)
plt.title('Segmented Image')
plt.show()

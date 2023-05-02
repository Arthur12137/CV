import cv2

def on_threshold1_trackbar(val):
    global threshold1
    threshold1 = val
    update_edges()

def on_threshold2_trackbar(val):
    global threshold2
    threshold2 = val
    update_edges()

def update_edges():
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

    # Perform Canny edge detection
    edges = cv2.Canny(blurred_image, threshold1, threshold2)

    # Display the edges
    cv2.imshow('Edges', edges)

# Load the image
image_path = 'u_L.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded
if image is None:
    raise ValueError("Image not found or could not be loaded.")

# Set initial values
kernel_size = 5
sigma = 1.0
threshold1 = 50
threshold2 = 150

# Create a window
cv2.namedWindow('Edges')

# Create trackbars
cv2.createTrackbar('Threshold1', 'Edges', threshold1, 255, on_threshold1_trackbar)
cv2.createTrackbar('Threshold2', 'Edges', threshold2, 255, on_threshold2_trackbar)

# Check if the kernel size is odd, if not, make it odd
if kernel_size % 2 == 0:
    kernel_size += 1

# Display the edges initially
update_edges()

# Wait for user input and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

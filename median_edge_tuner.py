import cv2

def on_image_selection_trackbar(val):
    global image, image_path
    image_path = image_paths[val]
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    update_edges()


def on_kernel_size_trackbar(val):
    global kernel_size
    kernel_size = val
    if kernel_size % 2 == 0:
        kernel_size += 1
    update_edges()

def on_sigma_trackbar(val):
    global sigma
    sigma = val / 10
    update_edges()

def on_threshold1_trackbar(val):
    global threshold1
    threshold1 = val
    update_edges()

def on_threshold2_trackbar(val):
    global threshold2
    threshold2 = val
    update_edges()

def on_blur_method_trackbar(val):
    global blur_method
    blur_method = val
    update_edges()

def save_edges():
    output_path = 'edge_output.png'
    cv2.imwrite(output_path, current_edges)
    print(f"Edges saved to {output_path}")

def update_edges():
    global current_edges
    # Apply the chosen blur method
    if blur_method == 0:
        blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    else:
        blurred_image = cv2.medianBlur(image, kernel_size)

    # Perform Canny edge detection
    current_edges = cv2.Canny(blurred_image, threshold1, threshold2)

    # Display the edges
    cv2.imshow('Edges', current_edges)

    # Print the current parameter values
    blur_name = 'Gaussian' if blur_method == 0 else 'Median'
    print(f"Blur Method: {blur_name}, Kernel Size: {kernel_size}, Sigma: {sigma}, Threshold1: {threshold1}, Threshold2: {threshold2}")

# Load the image
image_paths = ['u_L.png', 'u_R.png']
image_path = image_paths[0]
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded
if image is None:
    raise ValueError("Image not found or could not be loaded.")

# Set initial values
kernel_size = 5
sigma = 1.0
threshold1 = 50
threshold2 = 150
blur_method = 0  # 0 for Gaussian, 1 for Median

# Create a window
cv2.namedWindow('Edges')

# Create trackbars
cv2.createTrackbar('Image', 'Edges', 0, len(image_paths) - 1, on_image_selection_trackbar)
cv2.createTrackbar('Kernel Size', 'Edges', kernel_size, 20, on_kernel_size_trackbar)
cv2.createTrackbar('Sigma x10', 'Edges', int(sigma * 10), 50, on_sigma_trackbar)
cv2.createTrackbar('Threshold1', 'Edges', threshold1, 255, on_threshold1_trackbar)
cv2.createTrackbar('Threshold2', 'Edges', threshold2, 255, on_threshold2_trackbar)
cv2.createTrackbar('Blur Method', 'Edges', blur_method, 1, on_blur_method_trackbar)

# Display the edges initially
current_edges = update_edges()

# Wait for user input and close the windows
while True:
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        save_edges()
    elif k == 27:  # Press 'ESC' to exit
        break

cv2.destroyAllWindows()

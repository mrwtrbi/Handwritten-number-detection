import cv2
import numpy as np
import matplotlib.pyplot as plt

# Replace 'your_image.jpg' with the actual path to your image file
image_path = 'H:\Documents\MnistExamples.png'

   

# Load the image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print(f"Error: Unable to load the image at {image_path}")
else:
    #Remove noise by blurring with a Gaussian filter
    image = cv2.GaussianBlur(image, (3, 3), 0)
    # Convert the image to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply the Laplacian filter
    laplacian = cv2.Laplacian(image_gray, cv2.CV_64F)
    
   # Apply a threshold to detect zero crossings
    threshold = 0.1
    edges = cv2.threshold(np.abs(laplacian), threshold, 255, cv2.THRESH_BINARY)[1]

    # Display the results
    plt.subplot(131), plt.imshow(image_gray, cmap='gray'), plt.title('Original Image')
    plt.subplot(132), plt.imshow(np.abs(laplacian), cmap='gray'), plt.title('Laplacian')
    plt.subplot(133), plt.imshow(edges, cmap='gray'), plt.title('Detected Edges')
    plt.show()
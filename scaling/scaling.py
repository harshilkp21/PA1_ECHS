import cv2

# Load image
img = cv2.imread("robot.png")
if img is None:
    print("Image not found! Place 'input.jpg' in the same folder.")
    exit()

print("Original Dimensions:", img.shape)

# ----- Downscaling (high quality) -----
downscale = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv2.INTER_AREA)

# ----- Upscaling (high quality) -----
upscale = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2), interpolation=cv2.INTER_CUBIC)

# Save results
cv2.imwrite("downscaled.jpg", downscale)
cv2.imwrite("upscaled.jpg", upscale)

# Show results
cv2.imshow("Original", img)
cv2.imshow("Downscaled", downscale)
cv2.imshow("Upscaled", upscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

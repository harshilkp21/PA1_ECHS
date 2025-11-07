import cv2
import numpy as np

# ---------- READ ORIGINAL IMAGE ----------
img = cv2.imread("/home/harshil/PA1_ECHS/blurr/robot.png")
if img is None:
    raise Exception("robot.png not found")

# ---------- BLUR IMAGE ----------
blurred = cv2.GaussianBlur(img, (15, 15), 0)
cv2.imwrite("/home/harshil/PA1_ECHS/blurr/blurred.jpg", blurred)
print("✅ Blurred image saved as blurred.jpg")

# ---------- UNBLUR (Sharpen) ----------
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

unblurred = cv2.filter2D(blurred, -1, kernel)
cv2.imwrite("/home/harshil/PA1_ECHS/blurr/unblurred.jpg", unblurred)
print("✅ Unblurred image saved as unblurred.jpg")

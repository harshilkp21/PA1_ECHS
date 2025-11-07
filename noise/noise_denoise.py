import cv2
import numpy as np

# ---------- READ ORIGINAL IMAGE ----------
img = cv2.imread("/home/harshil/PA1_ECHS/noise/robot.png")
if img is None:
    raise Exception("robot.png not found")

# ---------- ADD NOISE ----------
noise = np.random.normal(0, 25, img.shape).astype(np.uint8)
noised = cv2.add(img, noise)
cv2.imwrite("/home/harshil/PA1_ECHS/noise/noised.jpg", noised)
print("✅ Noised image saved as noised.jpg")

# ---------- REMOVE NOISE (DENOISE) ----------
denoised = cv2.GaussianBlur(noised, (5, 5), 0)
cv2.imwrite("/home/harshil/PA1_ECHS/noise/denoised.jpg", denoised)
print("✅ Denoised image saved as denoised.jpg")

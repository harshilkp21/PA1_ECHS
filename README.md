# PA1_ECHS

This project contains three basic image processing tasks:
1. Image Scaling
2. Image Blurring & Unblurring
3. Image Noising & Denoising

Each task is kept in its own folder with Python code and image outputs.

---

## ✅ 1. Scaling (scaling folder)
**Scaling** means changing the size of an image:
- **Upscaling** = increasing the image size
- **Downscaling** = decreasing the image size

The file `scaling.py` reads an original image and produces:
- `downscaled.jpg`
- `upscaled.jpg`

---

## ✅ 2. Blurring & Unblurring (blurr folder)
**Blurring** means reducing the sharpness of an image.  
It is done using a **Gaussian Blur**, which smoothens the pixels.

**Unblurring** means sharpening the blurred image using a filter (kernel).

The file `blur_unblur.py`:
- takes `original.jpg`
- creates `blurred.jpg`
- then sharpens it to create `unblurred.jpg`

---

## ✅ 3. Noise & Denoise (noise folder)
**Noise** means random dots/grains added to an image (looks like disturbance).  
We add Gaussian noise.

**Denoising** means cleaning the noise.  
We use **Gaussian Blur** to remove the noise.

The file `noise_denoise.py`:
- takes `original.jpg`
- generates `noised.jpg`
- then removes noise to create `denoised.jpg`

---

## ✅ How to Run Each Program

Go inside the folder, then run the Python file:

### Scaling:
```bash
cd scaling
python3 scaling.py
```
### Blurring & Unblurring:
```bash
cd blurr
python3 blur_unblur.py
```
### Noise & Denoise:
```bash
cd noise
python3 noise_denoise.py
```

✅ Requirements

Python 3
OpenCV (pip install opencv-python)
NumPy (pip install numpy)

✅ Project Structure

PA1_ECHS/
│
├── scaling/
│   └── scaling.py
│
├── blurr/
│   ├── original.jpg
│   └── blur_unblur.py
│
└── noise/
    ├── original.jpg
    └── noise_denoise.py

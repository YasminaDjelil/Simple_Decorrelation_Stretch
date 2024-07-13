import numpy as np
import matplotlib.pyplot as plt
import cv2

def decorrelation(image_path, crop_coords=None, rotate=False, save_=False):

    img = cv2.imread(image_path)
    if crop_coords:
        x, y, w, h = crop_coords
        img = img[y:y+h, x:x+w]

    if rotate:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # in case of Specim IQ
    
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    ca = clahe.apply(a)
    cb = clahe.apply(b)
    enhanced_lab = cv2.merge((cl, ca, cb))
    enhanced_img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
    
    plt.figure(figsize=(12, 10))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2RGB))
    plt.show()

    if save_:
        save_path_with_extension = image_path + '_Decorrelation.png'
        cv2.imwrite(save_path_with_extension, enhanced_img)
        print(f"Enhanced image saved to {save_path_with_extension}")


# example
image_path = 'path/to/image' 
dstretch(image_path, crop_coords=(50, 0, 200, 450), rotate=True, save_=True)

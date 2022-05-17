# thumbnail 70/100
# large 1657 × 2366
# normal 

import os
import sys
from turtle import right
import cv2


def resize_thumb_thesis(img,i):
    scale_percent = 10 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
  
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    scale_percent = 100 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    maini = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print(resized.shape)
    cv2.imwrite(os.path.join(sys.argv[2], f'{i}-thumb'+ '.jpg'), resized)
    cv2.imwrite(os.path.join(sys.argv[2], f'{i}-large'+ '.jpg'), img)
    cv2.imwrite(os.path.join(sys.argv[2], f'{i}'+ '.jpg'), maini)

def resize_thumb(img,i):
    scale_percent = 50 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
  
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print(resized.shape)
    if i:
        cv2.imwrite(os.path.join(sys.argv[2], f'{i}-thumb'+ '.jpg'), resized)
        cv2.imwrite(os.path.join(sys.argv[2], f'{i}-large'+ '.jpg'), img)
        cv2.imwrite(os.path.join(sys.argv[2], f'{i}'+ '.jpg'), img)

def main():
    os.makedirs(sys.argv[2], exist_ok=True)
    print(os.listdir(sys.argv[1])[0][:-3])
    images = sorted(os.listdir(sys.argv[1]), key=lambda x: x)
    i = 0
    for image in images:
        img = cv2.imread(os.path.join(sys.argv[1], image))
        height, width, channels = img.shape
        resize_thumb_thesis(img,i+1)
        i += 1
        # left_image, right_image = img[:, :width//2, :], img[:, width//2:, :]
        # print(left_image.shape, right_image.shape , img.shape)
        
        # resize_thumb(left_image,i)
        # i += 1
        # resize_thumb(right_image,i)
        # i+=1
    pass


if __name__ == '__main__':
    main()
    sys.exit(0)

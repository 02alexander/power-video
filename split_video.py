#!/usr/bin/env python3

import cv2
import numpy as np
import sys

def main():
    video_path = sys.argv[1]
    dir_path = sys.argv[2]
    if dir_path[-1] != '/':
        dir_path = dir_path + '/'

    cap = cv2.VideoCapture(video_path)
    for i in range(100000000):
        if i % 6 != 0:
            continue
        _,img = cap.read()
        cv2.imwrite(f'{dir_path}{i}.png', img)
    

if __name__=="__main__":
    main()
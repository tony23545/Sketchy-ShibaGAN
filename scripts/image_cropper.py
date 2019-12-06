import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import numpy as np
import cv2
import os

in_path = "../flickr_output/shiba inu/"
out_path = "../crop_image/"

if not os.path.exists(out_path):
    os.makedirs(out_path)

drawing = True
save = False
point = (0,0)

half_size = 192

def mouse_drawing(event, x, y, flags, params):
    global point, drawing, save
    if event == cv2.EVENT_LBUTTONDOWN:
        save = True
    elif event == cv2.EVENT_MOUSEMOVE:
        point = (x, y)

def main():
    global point, drawing, save
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_drawing)
    count = 0
    for image_path in os.listdir(in_path):
        input_path = os.path.join(in_path, image_path)
        img = cv2.imread(input_path)

        while True:
            frame = img.copy()
            if drawing:
                cv2.rectangle(frame,(point[0]-half_size, point[1]-half_size),(point[0]+half_size, point[1]+half_size),(0,0,255),0)
            cv2.imshow("image", frame)
            key = cv2.waitKey(50)
            if key == ord('d'):
                os.remove(input_path)
                break
            if save:
                try:
                    cv2.imwrite(os.path.join(out_path, image_path), img[point[1]-half_size:point[1]+half_size,  point[0]-half_size:point[0]+half_size])
                except:
                    print("abort")
                save = False
                count+=1
                print("save %d image" % count)
                break

if __name__ == "__main__":
    main()
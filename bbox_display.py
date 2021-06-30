import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
import random

def load_display(img_filename, line_size = 2):
    # 
    json_path = "./Data/" + img_filename + '.json'
    img_path = "./source/" + img_filename + '.jpg'
    
    print(json_path, img_path)
    
    img = cv2.imread(img_path)
    bbox_img = img.copy()
    
    with open(json_path, "r", encoding='utf-8-sig') as fp_json:
        json_file = json.load(fp_json)
        for idx, box_data in enumerate(json_file):
            # box pos data: (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
            top_left = tuple(box_data['box'][:2])
            bottom_right = tuple(box_data['box'][-2:])
            # def => cv2.rectangle(img, start, end, color, thickness)
            box_color = (random.randrange(100,255),random.randrange(100,255),random.randrange(100,255))
            bbox_img = cv2.rectangle(bbox_img, top_left, bottom_right, box_color, line_size)
    # display
    plt.imshow(bbox_img)
    
    # return bbox_img
import numpy as np


def clean_boxes(boxes, img_width, img_height):
    cleaned_boxes = []
    for box in boxes:
        x1,y1,x2,y2 = box

        if x2 < x1:
            x1,x2 = x2,x1
        if y2 < y1:
            y1,y2 = y2,y1

        x1 = np.clip(x1,0, img_width-1)
        x2 = np.clip(x2,0, img_width-1)
        y1 = np.clip(y1,0, img_height-1)
        y2 = np.clip(y2,0, img_height-1)

        if x2>x1 and y2>y1:
            cleaned_boxes.append((x1,y1,x2,y2))
    return cleaned_boxes


boxes = [
    [50, 50, 100, 100],     # valid
    [120, 80, 110, 130],    # negative width -> will swap
    [-10, 20, 30, 50],      # partially outside -> clipped
    [200, 200, 150, 150],   # negative width & height -> swap -> valid
    [300, 300, 290, 290]    # invalid after swap -> removed
]

cleaned = clean_boxes(boxes, 255,255)
print(cleaned)
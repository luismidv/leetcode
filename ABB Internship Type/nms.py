"""
NON MAX SUPRRESSION
Given a list of bounding boxes with confidence scores,
remove overlapping boxes that correspond to the same object, keeping only the most confident one.
"""
import numpy as np

def iou(box1, box2):
    """
    Intersection over union between two bounding boxes.
    :param box1: First bounding box
    :param box2: Second bounding box
     """

    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    inter_w = max(0, x2 - x1)
    inter_h = max(0, y2 - y1)
    inter_area = inter_w * inter_h

    #UNION
    area_1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area_2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union = area_1 + area_2 - inter_area

    return inter_area / union

def nms (bboxes, scores, iou_threshold = 0.5):
    """
    HERE WE ARE ASSUMING THAT EACH BBOX HAS ALREADY PASSED THE NECCESARY THRESHOLD SO EVERY BBOX SHOULD BE > 0.5
    """
    if (len(bboxes) == 0):
        return []

    boxes = np.array(bboxes)
    scores = np.array(scores)

    scores = np.argsort(scores)[::-1]
    keep = []

    while len(scores) > 0:
        i = scores[0]
        keep.append(i)

        ious = np.array([])





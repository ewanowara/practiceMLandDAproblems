'''
Given two bounding boxes, output the intersection over union
'''

import numpy as np
def iou(bbox_pred, bbox_true):

    # bbox - x, y, w, h 

    x1 = bbox_pred[0]
    y1 = bbox_pred[1]
    w1 = bbox_pred[2]
    h1 = bbox_pred[3]

    x2 = bbox_true[0]
    y2 = bbox_true[1]
    w2 = bbox_true[2]
    h2 = bbox_true[3]

    intersection = (max([x1, x2]) - min( [x1+w1, x2+w2] )) * (max([y1,y2]) - min( [y1+h1 , y2+h2])) 

    union = w1*h1 +w2*h2 - intersection

    iou_result = intersection/union

    return iou_result

if __name__ == "__main__":
    # Example   
    bbox_pred = np.array([0,0,10,10])
    bbox_true = np.array([5,5,15,20])

    iou_out = iou(bbox_pred, bbox_true)
    print(iou_out)
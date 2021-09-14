from pathlib import Path

import cv2
import numpy as np
import os


def accuracy(prediction_mask, mask):
    print("accuracy calculating...")

    TP = 0
    FP = 0
    TN = 0
    FN = 0
    print(len(prediction_mask))
    print(len(mask))
    for i in range(0, prediction_mask.shape[0]):
        for j in range(0, prediction_mask.shape[1]):

            if prediction_mask[i][j] == mask[i][j]:
                if prediction_mask[i][j] == 255:
                    TP += 1
                else:
                    TN += 1
            else:
                if prediction_mask[i][j] == 255:
                    FP += 1
                else:
                    FN += 1

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    accuracy = 2 * precision * recall / (precision + recall)

    print('Accuracy:', accuracy)

    print("accuracy calculated!")
    return accuracy


def check(mask1, prediction_mask1):
    print(mask1)
    #mask1=Path(mask1)
    #prediction_mask1=Path(prediction_mask1)
    #cv2.imshow('image',mask1)
    mask = cv2.imread(mask1)
    prediction_mask = cv2.imread(prediction_mask1)
    mask_gray = cv2.cvtColor(mask, cv2.COLOR_RGB2GRAY)
    mask = np.array(mask_gray)
    prediction_mask_gray = cv2.cvtColor(prediction_mask, cv2.COLOR_RGB2GRAY)
    prediction_mask = np.array(prediction_mask_gray)
    imgaccuracy=accuracy(prediction_mask, mask)
    return imgaccuracy

#check('forged1.png','forged1_mask.png')

def getfolder():
    accuracy_list=[]
    package_dir = os.path.dirname(os.path.abspath(__file__))
    print(package_dir)
    dir = str(package_dir)
    dir = dir.replace('\\', '//')
    print(dir)
    mask1folder = dir[:-7]+"//templates//images//Sample_masks//"
    mask2folder = dir[:-7]+"//templates//images//System_masks//"
    sample = next(os.walk(mask1folder))[2]  # dir is your directory path as string
    system = next(os.walk(mask2folder))[2]
    print(sample)
    # for x in onlyfiles:
    #    print(x)

    for x in sample and system:
        imgename=str(x)
        mask1addrs=mask1folder+imgename
        mask2addrs=mask2folder+imgename
        accuracy=check(mask1addrs,mask2addrs)
        accuracy_list.append(accuracy)
    avg=sum(accuracy_list)/len(accuracy_list)
    return avg


#getfolder()
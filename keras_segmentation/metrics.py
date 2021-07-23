import numpy as np
import tensorflow as tf

EPS = 1e-12


def get_iou(gt, pr, n_classes):
    class_wise = np.zeros(n_classes)
    for cl in range(n_classes):
        intersection = np.sum((gt == cl)*(pr == cl))
        union = np.sum(np.maximum((gt == cl), (pr == cl)))
        iou = float(intersection)/(union + EPS)
        class_wise[cl] = iou
    return class_wise

#dice coefficient implementation
def dice_coef(y_true, y_pred, smooth=1):
    intersection = tf.sum(y_true * y_pred, axis=[1,2,3])
    union = tf.sum(y_true, axis=[1,2,3]) + tf.sum(y_pred, axis=[1,2,3])
    return tf.mean( (2. * intersection + smooth) / (union + smooth), axis=0)

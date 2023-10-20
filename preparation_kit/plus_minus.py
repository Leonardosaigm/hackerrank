import math
import os
import random
import re
import sys


def plusMinus(arr):
    negatives = 0
    positives = 0
    zeros = 0

    for num in arr:
        if num < 0:
            negatives += 1
        elif num > 0:
            positives += 1
        elif num == 0:
            zeros += 1

    print("%.6f" % (positives/len(arr)))
    print("%.6f" % (negatives/len(arr)))
    print("%.6f" % (zeros/len(arr)))



arrey = [-4, 3, -9, 0, 4, 1]

plusMinus(arrey)
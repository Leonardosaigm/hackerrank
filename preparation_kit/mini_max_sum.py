import math
import os
import random
import re
import sys

def miniMaxSum(arr):       
    sort = sorted(arr)
    minimun = sum(sort[0:4])
    maximum = sum(sort[1:5])

    print(f'{minimun} {maximum}')


arrey = [1, 3, 5, 7, 9]

miniMaxSum(arrey)

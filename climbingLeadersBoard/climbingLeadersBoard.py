#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.


def climbingLeaderboard(scores, alice):


    scoresArray = list(scores)
    scoresArray.sort(reverse=True)
    limiting_position = len(scoresArray)-1
    for points in alice:
        if points < scoresArray[len(scoresArray) - 1]:
            print(len(scoresArray) + 1)

            continue
        elif points >= scoresArray[0]:

            print(1)

            continue
        else:

            for position in range(0,limiting_position):
                if (points >= scoresArray[position+1] and points < scoresArray[position]):
                    limiting_position = position + 1
                    print(position+2)





if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

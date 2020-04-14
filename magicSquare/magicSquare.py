import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.


def formingMagicSquare(s):
    all_possible = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]], ]
      arrayOfValue = []
       for elements in all_possible:
            # print(elements)
            value = 0
            for r in range(3):
                for c in range(3):
                    # print(elements[r][c])
                    # print(s[r][c])
                    value += abs(elements[r][c] - s[r][c])
            arrayOfValue.append(value)
        print(min(arrayOfValue))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    def formingMagicquare(a)

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

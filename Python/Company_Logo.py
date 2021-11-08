'''
Company Logo
https://www.hackerrank.com/challenges/most-commons/problem
'''

from collections import Counter
from itertools import groupby


def main():
    S = input()
    result = []

    for _, items in groupby(Counter(S).most_common(len(set(S))), key=lambda x: x[1]):

        for element in sorted(items, key=lambda x: x[0]):
            result.append(element)

    for item in result[:3]:
        print(item[0], item[1])


if __name__ == "__main__":
    main()

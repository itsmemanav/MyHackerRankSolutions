'''
Athlete Sort
https://www.hackerrank.com/challenges/python-sort-sort/problem
'''


def main():

    N, M = [int(i) for i in input().split()]
    inp = []

    for i in range(N):
        inp.append([int(i) for i in input().split()])

    K = int(input())

    raw_org = list(zip(inp, [z for z in range(len(inp))]))

    mapped_org = list(map(lambda x: (x[0][K], x[1]), raw_org))

    result_mapped_org = sorted(mapped_org, key=lambda x: x[0])

    for element in result_mapped_org:
        print(" ".join([str(item) for item in raw_org[element[1]][0]]))


if __name__ == "__main__":
    main()

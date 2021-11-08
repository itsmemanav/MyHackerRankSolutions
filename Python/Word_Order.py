'''
Word Order
https://www.hackerrank.com/challenges/word-order/problem

'''


def main():

    n, map_inp = int(input()), dict()

    for i in range(n):
        r = input()
        if r not in map_inp.keys():
            map_inp[r] = 1
        else:
            map_inp[r] += 1

    print(len(map_inp))
    for key in map_inp.keys():
        print(map_inp[key], end=" ")


if __name__ == "__main__":
    main()

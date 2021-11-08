'''
Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem
'''


def merge_the_tools(string, k):
    subsequence = [string[i:i+k] for i in range(0, len(string), k)]

    for seq in subsequence:
        result = ""
        for char in seq:
            if char not in result:
                result += char
        print(result)


if __name__ == '__main__':
    string, k = input("> "), int(input("> "))
    merge_the_tools(string, k)

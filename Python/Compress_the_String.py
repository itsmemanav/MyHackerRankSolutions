'''
Compress the String!
https://www.hackerrank.com/challenges/compress-the-string/problem
'''


def main():

    inp = input()
    count, result, length = 1, [], len(inp)

    if length == 1:
        result.append(f"{(1, int(inp[0]))}")

    else:
        for index in range(length-1):
            if inp[index] == inp[index + 1]:
                count += 1
            else:
                result.append(f"{(count, int(inp[index]))}")
                count = 1

        # Edge case handling
        if inp[-1] == inp[-2]:
            result.append(f"{(count, int(inp[-2]))}")
        else:
            result.append(f"{(1, int(inp[-1]))}")

    print(" ".join(result))


if __name__ == "__main__":
    main()

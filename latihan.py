# binary to decimal

input = 100


def binaryToDecimal(input):
    binaryValue = str(input)
    result = 0
    temp = 1
    for i in range(len(binaryValue) - 1, -1, -1):
        result += int(binaryValue[i]) * temp
        temp = temp * 2
    return result


print(binaryToDecimal(input))

# binary to decimal

input = 111


def binaryToDecimal(input):
    str_input = str(input)
    temp = 1
    result = 0
    for i in range(len(str_input)-1, -1, -1):
        result += int(str_input[i]) * temp
        temp *= 2

    return result


print(binaryToDecimal(input))


# Sort using bubble

# array1 = [5, 1, 2, 4, 5]
# array2 = [9, 2, 4, 5, 10, 20, 30]

# merge = array1 + array2

# for i in range(0, len(merge)):
#     temp = 0
#     for j in range(0, len(merge)-i-1):
#         if (merge[j] > merge[j+1]):
#             temp = merge[j]
#             merge[j] = merge[j+1]
#             merge[j+1] = temp

# print(merge)

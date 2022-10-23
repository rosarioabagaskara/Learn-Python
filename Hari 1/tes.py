# row = 10
# print("Half triangle")
# for i in range(0, row):
#     for j in range(0, i+1):
#         print("*", end="")
#     print("\n")
# row = 10
# print("reverse Half Triangle")
# print()
# for i in range(row, 0, -1):
#     for j in range(0, i):
#         print("*", end="")
#     print("\n")

# row = 10
# for i in range(0, row):
#     for j in range(0, row):
#         print(" ", end="")
#     for k in range(0, i):
#         print("*", end="")
#     row = row - 1
#     print("\n")

# row = 10
# for i in range(0, row):
#     for j in range(0, i):
#         print(" ", end="")
#     for k in range(0, row):
#         print("*", end="")
#     row = row - 1
#     print("\n")

# row = 10
# for i in range(0, row):
#     for j in range(0, i):
#         print("", end=" ")
#     for k in range(0, row):
#         print("*", end=" ")
#     row = row - 1
#     print("\n")

# row = 10
# for i in range(0, row):
#     for j in range(0, row):
#         print("", end=" ")
#     for k in range(0, i):
#         print("*", end=" ")
#     row = row - 1
#     print()


# print("decimal to binary")


# def converDectoBinary(decimalValue):
#     if decimalValue > 1:
#         converDectoBinary(decimalValue//2)
#     print(decimalValue % 2, end="")


# converDectoBinary(3)


# tesRow = 10

# for a in range(0, tesRow):
#     for c in range(0, a):
#         print("", end="*")
#     for b in range(0, tesRow):
#         print("*", end=" ")
#     tesRow -= 1
#     print()

# row = 10
# for i in range(0, row):
#     for j in range(0, i):
#         print("", end=" ")
#     for k in range(0, row):
#         print("*", end=" ")
#     row = row - 1
#     print("\n")

# def dectobinary(number):
#     if number > 1:
#         dectobinary(number // 2)
#     print(number % 2)


# dectobinary(10)


def decBinary(numbers):
    if numbers > 1:
        decBinary(numbers//2)
    print(numbers % 2, end="")


decBinary(10)

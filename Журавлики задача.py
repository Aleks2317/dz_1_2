# s = int(input())
# a = s / 6
# b = a
# c = s - a - b
# print(int(a), int(c), int(b))

count = int(input())
petia = count / 6
serj = petia
katrin = count - petia - serj
print(int(petia), int(katrin), int(serj))


# z, n, a, b = map(int, input().split())
# s = float((z + n + a + b) / 4)
# print(s)
# def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
#     matrica = []
#     lin = 0
#     for i in range(size):
#         matrica.append([0]*size)
#     for i in range(size):
#         for j in range(size):
#             if i == j:
#                 lin += 1
#                 matrica[i][j] = lin
#             elif i < j:
#                 matrica[i][j] = up_fill
#             elif i > j:
#                 matrica[i][j] = down_fill
#     return matrica
#
# print(create_matrix(up_fill=7))
#
# s = input()
# print(s.lower().startswith('mam'))
# s = input()
# print(s.lower().startswith('mam'))

# def tribonacci(n):
#     if n in (0, 1):
#         return 0
#     if n == 2:
#         return 1
#     return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
# print(tribonacci(8))
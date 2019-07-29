arr = [55, 7, 78, 12, 42]


# 버블 정렬
# n = len(arr)
#
# for j in range(n - 1, 0, -1):
#     for i in range(j):
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
# print(arr)


# 선택 정렬
# min_idx = 0
# for j in range(len(arr) - 1):
#     for i in range(j, len(arr)):
#         if arr[i] < arr[min_idx]:
#             min_idx = i
#     arr[j], arr[min_idx] = arr[min_idx], arr[j]
# print(arr)


# counting 정렬
data = [0, 3, 1, 3, 1, 2, 4, 1]
counts = [0] * 5    # 최대값 = 4
for value in data:
    counts[value] += 1

# sorted_list = []
# for i in range(len(counts)):
#     for j in range(counts[i]):
#         sorted_list.append(i)
# print(sorted_list)

    # 누적빈도수
for i in range(1, len(counts)):
    counts[i] = counts[i - 1] + counts[i]
sorted_list = []


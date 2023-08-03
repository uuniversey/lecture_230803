

# 부분집합 생성하기1 - 이 방법대로는 너무 복잡해지게 된다.

# def print_subset(bit, arr, n):
#     total = 0
#     for i in range(n):
#         if bit[i]:
#             print(arr[i], end = ' ')
#             total += arr[i]
#     print (bit)
#     print (total)
#
# arr = [1,2,3,4]
# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print_subset(bit, arr, 4)



# 부분집합 생성하기2 - 보다 간결하게 부분집합을 생성

# arr = [3,6,7,1,5,4]
# # arr = [1,2,3]
#
# n = len(arr)
#
# for i in range(1<<n) :
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=', ')
#     print()



# 이진 검색(Binary Search)

# def binarySearch(a, N, key):
#     start = 0
#     end = N-1
#     while start <= end :
#         middle = (start + end)//2
#         if a[middle] == key:    # 검색 성공
#             return True
#         elif a[middle] > key:
#             end = middle - 1
#         else:
#             start = middle + 1
#     return false                # 검색 실패



# 선택 정렬 과정

# def selectionSort(a, N):
#     for i in range(N-1):        # 마지막은 자기끼리 교환하는거니까 N까지 갈 필요 없고 N-1
#         minIdx = i
#         for j in range(i+1, N):
#             if a[minIdx] > a[j]:
#                 minIdx = j
#         a[i], a[minIdx] = a[minIdx], a[i]
#     return a
#
# a = [64, 25, 10, 22, 11]
# print(selectionSort(a, 5))


# test


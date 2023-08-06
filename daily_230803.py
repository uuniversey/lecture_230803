

# 1210. 2일차 - Ladder1

# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(100)]
#
#     for col in range(100):
#         if arr[99][col] == 2:                 # x(2)를 찾고 x에서의 idx값을 설정.
#             idx = col
#             start_point = 0
#             break
#
#     for row in range(99, -1, -1):
#         if row == 0:
#             start_point = idx
#
#         elif idx-1 < 0 or idx+1 > 99:           # 예외 처리 - 0번 인덱스
#             if idx-1 < 0:
#                 if arr[row][idx+1] == 1:
#                     while arr[row - 1][idx + 1] == 0:
#                         idx += 1
#                     idx += 1
#                 else:
#                     continue
#
#             elif idx+1 > 99:                     # 예외 처리 - 99번 인덱스
#                 if idx+1 > 99:
#                     if arr[row][idx-1] == 1:
#                         while arr[row-1][idx-1] == 0:
#                             idx -= 1
#                         idx -= 1
#                     else:
#                         continue
#
#         elif arr[row][idx-1] == 1:               # 좌측 판별
#             if idx-1 == 0:
#                 idx = 0
#             else:
#                 while arr[row-1][idx-1] == 0:
#                     idx -= 1
#                 idx -= 1
#
#         elif arr[row][idx+1] == 1:               # 우측 판별
#             if idx+1 == 99:
#                 idx = 99
#             else:
#                 while arr[row-1][idx+1] == 0:
#                     idx += 1
#                 idx += 1
#
#         else:
#             continue
#
#     print(f'#{tc} {start_point}')



# 18124. 부분집합 합 문제 구현하기

# import sys
# sys.stdin = open('input_18124.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = list(map(int,input().split()))
#
#     n = len(arr)
#     isTrue = 0
#     for i in range(1<<n):                   # 집합의 개수
#         my_sum = 0
#         my_list = []
#         for j in range(n):                  # 부분집합 하나하나가 j for문을 돌면서 나온다 i개 만큼
#             if i & (1<<j):
#                 my_list.append(arr[j])
#
#         if len(my_list) == 0:
#             continue
#         else:
#             for k in my_list:
#                 my_sum += k
#             if my_sum == 0:
#                 isTrue = 1
#             else:
#                 my_list = []
#                 continue
#
#     print(f'#{tc} {isTrue}')



# 18060. 2일차 - 부분집합의 합

# import sys
# sys.stdin = open('input_4837.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int,input().split())
#     arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
#     n = len(arr)
#
#     my_sum = 0
#     isTrue = 0
#     for i in range(1<<n):                   # 집합의 개수
#         my_list = []
#         for j in range(n):                  # 부분집합 하나하나가 j for문을 돌면서 나온다 i개 만큼
#             if i & (1<<j):
#                 my_list.append(arr[j])
#
#         if len(my_list) == N:
#             for k in my_list:
#                 my_sum += k
#
#             if my_sum == K:
#                 isTrue += 1
#             else:
#                 my_sum = 0
#         else:
#             continue
#
#     print(f'#{tc} {isTrue}')



# 4839. 이진탐색

# import sys
# sys.stdin = open('input_4839.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     P, A ,B = map(int,input().split())
#     l = 1
#     r = P
#     center_A = int((l+r) / 2)
#     center_B = int((l+r) / 2)
#     count_A = 0
#     count_B = 0
#
#     while A != center_A:
#         if A > center_A:
#             l = center_A                        # 범위 줄여주기
#             center_A = int((center_A + r)/2)
#             count_A += 1
#
#         elif A < center_A:
#             r = center_A                         # 범위 줄여주기
#             center_A = int((l + center_A)/2)
#             count_A += 1
#
#     l = 1
#     r = P
#
#     while B != center_B:
#         if B > center_B:
#             l = center_B
#             center_B = int((center_B + r) / 2)
#             count_B += 1
#
#         elif B < center_B:
#             r = center_B
#             center_B = int((l + center_B)/2)
#             count_B += 1
#
#     if count_A > count_B:
#         winner = 'B'
#     elif count_A < count_B:
#         winner = 'A'
#     elif count_A == count_B:
#         winner = 0
#
#     print(f'#{tc} {winner}')



# 4843. 특별한 정렬

# import sys
# sys.stdin = open('input_4843.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     repeat = len(arr)
#     my_list = []
#     result_list = [0] * 10          # 0으로 채워진 리스트
#     min_v = 10000
#
#     for j in range(repeat):         # 오름차순 정렬
#         for i in arr:
#             if min_v > i:
#                 min_v = i
#         my_list.append(min_v)
#         arr.remove(min_v)
#         min_v = 10000
#
#     for k in range(10):             # 앞 뒤로 한개씩 번갈아 가면서 리스트화
#         if k % 2 == 0:
#             result_list[k] = my_list.pop()
#         else:
#             result_list[k] = my_list.pop(0)
#
#     print (f'#{tc}', *result_list)



# 1961. 숫자 배열 회전

import sys
sys.stdin = open('input_1961.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    my_box = [[0] * N for _ in range(N)]
    my_list = []
    sum_num = 0
    for col in range(N):
        sum_num = 0
        for row in range(N-1, -1, -1):
            sum_num += arr[row][col] * (10**row)
        my_list.append(sum_num)

    for col in range(N):
        for row in range(N):
            my_box[row][col] = my_list[row]

    print (f'#{tc} {my_box}')

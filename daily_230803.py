

# 1210. 2일차 - Ladder1

# import sys
# sys.stdin = open('input_m1.txt', 'r')
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(100)]
#
#     for j in range(100):
#         if arr[99][j] == 2:                 # x(2)를 찾고 x에서의 idx값을 설정해주고 left, right를 잡는다.
#             idx = j
#             left = idx - 1
#             right = idx + 1
#             start_point = 0
#             break
#
#
#
#
#
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

import sys
sys.stdin = open('input_4837.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    n = len(arr)

    my_sum = 0
    isTrue = 0
    for i in range(1<<n):                   # 집합의 개수
        my_list = []
        for j in range(n):                  # 부분집합 하나하나가 j for문을 돌면서 나온다 i개 만큼
            if i & (1<<j):
                my_list.append(arr[j])

        if len(my_list) == N:
            for k in my_list:
                my_sum += k

            if my_sum == K:
                isTrue += 1
            else:
                my_sum = 0
        else:
            continue

    print(f'#{tc} {isTrue}')










# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/28  17:41 
# 名称：最长上升子序列问题.PY
# 工具：PyCharm
"""
最长上升子序列（LIS）问题：给定长度为n的序列a，从a中抽取出一个子序列，这个子序列需要单调递增。
问最长的上升子序列（LIS）的长度。
　　e.g. 1,5,3,4,6,9,7,8的LIS为1,3,4,6,7,8，长度为6。
"""
if __name__ == '__main__':
    dp = [1, 5, 3, 4, 6, 9, 7, 8]
    arr = [1] * 6
    ans = -1
    for i in range(6):
        for j in range(6):
            if dp[j] < dp[i]:
                arr[i] = max(arr[i], arr[j] + 1)
        ans = max(arr[i], ans)
    print(ans)

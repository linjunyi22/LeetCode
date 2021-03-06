"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。
你可以返回满足此条件的任何数组作为答案。

示例：
输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
 
提示：
1. 1 <= A.length <= 5000
2. 0 <= A[i] <= 5000

"""


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for i in A:
        	if i%2 == 0:
        		result = [i] + result
        	else:
        		result.append(i)
        return result

test = Solution().sortArrayByParity([1,2,3,4])
print(test)

"""
Given two arrays, write a function to compute their intersection.

给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]

说明:
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        tmp = nums1_set if len(nums1_set) < len(nums2_set) else nums2_set
        
        return [i for i in tmp if i in nums2_set and i in nums1_set]

test = Solution().intersection([1,2,3],[1,2])
print(test)


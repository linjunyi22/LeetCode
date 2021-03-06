# 746. 使用最小花费爬楼梯
"""
数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
注意：

cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 动态规划
# 递推公式 f(n) = min(f(n-1),f(n-2)) + cost[i]
class Solution:
    # 使用数组的话空间复杂度为 O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])

    # 因为遍历过程中仅需要统计f(n-1),f(n-2)的值，因此 2 个变量即可
    # 空间复杂度可以到 O(1)
    def minCostClimbingStairs_1(self, cost: List[int]) -> int:
        f1, f2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            f1, f2 = f2, min(f1, f2) + cost[i]
        return min(f1, f2)

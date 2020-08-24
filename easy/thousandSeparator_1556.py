# 1556. 千位分隔数
"""
给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。
示例 1：

输入：n = 987
输出："987"
示例 2：

输入：n = 1234
输出："1.234"
示例 3：

输入：n = 123456789
输出："123.456.789"
示例 4：

输入：n = 0
输出："0"

提示：

0 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/thousand-separator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ""
        s = str(n)
        for i in range(len(s) - 1, -1, -3):
            if i <= 2:
                if len(res) == 0:
                    res = s[0:i+1]
                else:
                    res = s[0:i+1] + "." + res
                break
            else:
                if len(res) != 0:
                    res = s[i-2:i+1] + "." + res
                else:
                    res = s[i-2:i+1]
        return res

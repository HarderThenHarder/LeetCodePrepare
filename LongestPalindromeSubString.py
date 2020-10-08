"""
求最长回文子字符串问题。
"""


def main(s):
    """
    求字符串s中最长回文子字符串。
    :param s: 目标字符串
    :return: 最长回文子字符串
    """

    """ 创建二维表格，f(i, j)代表字符串s从i到j是否为一个回文字符串 """
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]

    longest_substring = ""
    max_length = 0

    """ 以索引j结尾/索引i开始的字符串 """
    for j in range(len(s)):
        for i in range(j+1):            # j取i+1是因为j可以等于i
            if j - i <= 1:
                """ 两个相邻字符是否可以组合成一个回文字符串 """
                if s[i] == s[j]:
                    dp[i][j] = True
                    if j-i+1 > max_length:
                        max_length = j-i+1
                        longest_substring = s[i:j+1]
            else:
                """ s[i]和s[j]相等，则判断s[i+1]~s[j-1]是否为回文字符串，若是回文则s[i]~s[j]也为回文字符串 """
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i+1 > max_length:
                        max_length = j-i+1
                        longest_substring = s[i:j+1]

    return longest_substring


def main2(s):
    """
    解法二，不使用dp数组，时间复杂度为o(n)。
    :param s: 目标字符串
    :return: 最长回文字符串长度
    """
    max_length = 1

    for i in range(1, len(s)):
        """ i-max_length 代表以i结尾的字符串，减掉目前最长的回文长度后，第一个字符索引是否为0，如果不为0就考虑把0索引字符加进去一起判断 """
        if i-max_length >= 1 and s[i-max_length-1:i+1] == s[i-max_length-1:i+1][::-1]:
            max_length += 2         # 如果子字符串为回文字符串，则总长度+2（添加了索引为0和索引为i的两个字符）
        elif i-max_length+1 >= 0 and s[i-max_length:i+1] == s[i-max_length:i+1][::-1]:
            max_length += 1         # 如果子字符串为回文字符串，则总长度+1（添加了索引为i的两个字符）

    return max_length


if __name__ == '__main__':
    print(main2('abbac'))

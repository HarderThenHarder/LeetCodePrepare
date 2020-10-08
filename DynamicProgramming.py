"""
动态规划问题
"""
import math


def coin_change(coins: list, amount: int):
    """
    硬币凑钱问题，给定一个总数amount，和一堆硬币coins，计算“最少”需要多少个硬币，若凑不到amount，返回-1.
    :param coins: 可选硬币列表
    :param amount: 总数
    :return: 硬币数
    """

    """ 构建dp数组，dp[i]代表所有硬币构成i块钱最少用多少个硬币 """
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0
    for i in range(1, len(dp)):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i-c]+1)

    res = int(dp[-1]) if dp[-1] != float('inf') else -1
    print("Coin Change: ", res)


def count_prime(n: int):
    """
    给定一个数n，返回这个数最少可以由多少个平方数相加得到，例如：
        4 = 1 + 1 + 1 + 1
        or
        4 = 2^2
    代表，4可以由4个1（1是平方数）组成，也可以由一个4（4是平方数）组成，因此答案返回1。
    :param n: 目标数
    :return: 平方数的个数
    """
    dp = [0 for _ in range(n+1)]                # 初始化dp数组，dp[i]代表i数字最少由多少个平方数相加

    for i in range(1, len(dp)):
        if math.sqrt(i) == int(math.sqrt(i)):   # 如果这个数本身是平方数，则设置为1
            dp[i] = 1
        else:
            min_v = float('inf')
            for j in range(1, i//2+1):          # dp[4] = dp[1] + dp[3] or dp[2] + dp[2]，求每一种组合情况中的最小值
                min_v = min(min_v, dp[j] + dp[i-j])
            dp[i] = min_v
    print("Count Prime: ", dp[-1])


def LIS(s: str):
    """
    求最长递增子序列的长度。
    :param s: 目标字符串
    :return: 最长递增子序列长度
    """
    dp = [1 for _ in range(len(s))]     # 建立dp数组，dp[i]表示以s[i]结尾的子字符串最长递增字串长度

    for i in range(1, len(dp)):
        lis_len = 1
        for j in range(i):
            if s[i] > s[j]:
                lis_len = max(lis_len, dp[j]+1)
        dp[i] = lis_len

    print("LIS: ", dp[-1])


def LCS(s1: str, s2: str):
    """
    寻找s1字符串和s2字符串中最长公共字符串的长度。
    :param s1: 目标字符串
    :param s2: 目标字符串2
    :return: 最长公共字符串长度
    """
    dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print("LCS: ", dp[-1][-1], end='   ->   ')

    """ 进一步计算出最长公共子字符串的内容 """
    i, j, res = len(s2), len(s1), ""
    while i >= 0 and j >= 0:
        if s1[j-1] == s2[i-1]:
            res += s1[j-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    print(res[::-1])


def max_value(weights: list, values: list, w: int):
    """
    0-1背包问题， 求解一个载重为w的背包可装的物品的最大价值是多少。
    :param w: 背包载重量
    :param weights: 物品重量列表
    :param values: 物品价值列表
    :return: 最大价值
    """

    """ 建立dp数组，dp[j]代表当前载重，dp[i]代表第i个物品，dp[i][j]代表当前载重且前i个物品可以装载的最大value """
    dp = [[0 for _ in range(w+1)] for _ in range(len(weights)+1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i-1][j]           # 不装物品i时的最大装载value
            if j - weights[i-1] >= 0:       # 若当前的背包载重装的下物品i
                dp[i][j] = max(dp[i][j], dp[i-1][j-weights[i-1]] + values[i-1])   # 取最大值

    print("0-1 Bag Problem: ", dp[-1][-1])


def max_value2(weights: list, values: list, items: list, w: int):
    """
    多重背包问题，和0-1背包问题相似，但区别在于每一种物品的数量不再是1，而是有限数量个，通过items列表得到，求最大价值。
    :param weights: 物品重量列表
    :param values: 物品价值列表
    :param items: 物品数量列表
    :param w: 背包装载量
    :return: 最大价值
    """
    weights = [0] + weights
    values = [0] + values
    items = [0] + items

    dp = [0] * (w+1)    # 构建dp数组，dp[i]代表当背包载量为i时可装的最大价值

    for i in range(1, len(items)):              # 遍历所有物品
        for j in range(w, weights[i]-1, -1):    # 从后往前开始逆向推，直到背包体积小于物品体积
            for k in range(1, min(items[i], j // weights[i]) + 1):  # 在dp[j]这里放入几个i物品的价值最大
                dp[j] = max(dp[j], dp[j - k * weights[i]] + k * values[i])

    print("Bag Problem with items count limit: ", dp[-1])


def min_edit_distance(s1: str, s2: str):
    """
    最小编辑距离问题，给定s1和s2两个字符串，求最少编辑次数。编辑方式：替换、增加、删除。
    :param s1: 目标字符串1
    :param s2: 目标字符串2
    :return: 最少编辑次数
    """

    """ 建立dp二维数组，dp[i][j]代表从s1[:j+1]和s2[:i+1]两个字符串的最小编辑距离 """
    dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

    """ 初始化第一行距离 """
    for i in range(len(dp[0])):
        dp[0][i] = i
    """ 初始化第一列距离 """
    for i in range(len(dp)):
        dp[i][0] = i

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1    # 分别代表替换、s2删除、s2增加

    print("Min Edit Distance: ", dp[-1][-1])


def can_partition_two_parts(arr: list):
    """
    一个数组，是否能将其分成两个部分，两部分的和相等。
        [1, 5, 11, 5] 可以分成 [1, 5, 5] 和 [11]，返回 True
        [1, 2, 3, 5] 无法分成两个相等的部分，返回 False
    这道题可以转换为0-1背包问题来解，求能否找到数组中若干个数的和等于sum(arr) // 2。
    :param arr: 目标数组
    :return: 布尔类型变量
    """
    sum_v = sum(arr)
    if sum_v % 2:
        print('Can Partition Two Parts: False')
        return
    sum_v = sum_v // 2

    """ 建立dp数组，dp[i][j]代表前i个数中是否可以凑出和为j的组合 """
    dp = [[False for _ in range(sum_v+1)] for _ in range(len(arr)+1)]

    """ 当不选择任何数的时候一定为False """
    for i in range(len(dp[0])):
        dp[0][i] = False
    """ 要凑出和为0的组合，直接所有数不选即可，因此全为True """
    for i in range(len(dp)):
        dp[i][0] = True

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i-1][j]       # 不选第i个物品时的情况
            if j - arr[i-1] >= 0 and dp[i-1][j-arr[i-1]]:
                dp[i][j] = True

    print("Can Partition Two Parts: ", dp[-1][-1])


def get_combinations(coins: list, n: int):
    """
    完全背包问题，给定一个硬币列表，每个硬币可以无限使用，n代表总值，问能凑成总值n一共有多少种凑法。
    如：
        coins = [1, 2, 5], n = 5, return 4, because:
        5 = 1 + 1 + 1 + 1 + 1
        5 = 2 + 1 + 1 + 1
        5 = 2 + 2 + 1
        5 = 5
    :param coins: 硬币列表
    :param n: 总数
    :return: 总共的组合数
    """

    """ 构建dp数组，dp[i][j]代表前i个硬币凑成j有多少种凑法 """
    dp = [[0 for _ in range(n+1)] for _ in range(len(coins)+1)]

    """ 当需要凑出的和为0时，不管硬币列表是什么样子都只有一种选择方法 """
    for i in range(len(dp)):
        dp[i][0] = 1

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if j - coins[i-1] >= 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]     # 注意这里是dp[i][j-coins[i-1]]，不是dp[i-1][...]是因为硬币i是可以无限使用的，若是dp[i-1][...]代表硬币i只能选择一次
            else:
                dp[i][j] = dp[i-1][j]

    print("Get Combinations: ", dp[-1][-1])


if __name__ == '__main__':
    coin_change([1, 2, 5], 11)
    count_prime(18)
    LIS('1435879')
    LCS("acbdjr", "jirecbdg")
    max_value([2, 1, 3], [4, 2, 3], 4)
    max_value2([3, 4, 5], [2, 3, 4], [4, 3, 2], 15)
    min_edit_distance("intention", "execution")
    can_partition_two_parts([1, 5, 11, 5])
    get_combinations([1, 2, 5], 5)
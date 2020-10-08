"""
打家劫舍问题合集
"""


def house_robber1(values: list):
    """
    给定一条街的value数组，要求不能打劫相邻的房间，求可打劫的最大价值。
    :param values: 街道价值数组
    :return: 最大收益
    """

    """ 建立dp数组，dp[i]代表前i个房间最多可获得多少收益 """
    dp = [0 for _ in range(len(values))]

    dp[0], dp[1] = values[0], values[1]

    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i-2]+values[i])

    print("[1] Max Value: ", dp[-1])


def house_robber2(values: list):
    """
    给定一条街的value数组，街道是环形街道（首尾相接），要求不能打劫相邻的房间，求可打劫的最大价值。
    :param values: 街道价值数组
    :return: 最大收益
    """

    def get_max_value(values: list):
        """
        不能打劫相邻的房间的最大值。
        :param values: 街道价值数组
        :return: 最大收益
        """
        dp = [0 for _ in range(len(values))]
        dp[0], dp[1] = values[0], values[1]

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + values[i])

        return dp[-1]

    """ 环形数组代表数组的首尾不能够一起取，和上个问题不同的就是首尾不能一起取，因此我们可以分别求取首和取尾的值，再求最大值。 """
    v1 = get_max_value(values[1:])      # 包含尾的情况
    v2 = get_max_value(values[:-1])     # 包含首的情况

    print("[2] Max Value: ", max(v1, v2))


if __name__ == '__main__':
    house_robber1([2, 7, 9, 3, 1])
    house_robber2([2, 3, 2])


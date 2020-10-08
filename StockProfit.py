"""
股票买卖问题
"""


def max_profit_with_one(prices: list):
    """
    给定一个价格数组，代表第i天的股票价格，只允许交易1次，买卖不能同时进行，问能获取的最高利润是多少。
    :param prices: 价格数组
    :return: 最大利润
    """
    min_v, max_p = prices[0], 0

    for i in range(1, len(prices)):
        if prices[i] < min_v:
            min_v = prices[i]
        else:
            max_p = max(max_p, prices[i] - min_v)

    print("Max profit1: ", max_p)


def max_profit_with_k(prices: list):
    """
    给定一个价格数组，代表第i天的股票价格，允许交易k次，买卖不能同时进行，问能获取的最高利润是多少。
    :param prices:
    :return:
    """


if __name__ == '__main__':
    max_profit_with_one([3, 2, 6, 5, 0, 3])
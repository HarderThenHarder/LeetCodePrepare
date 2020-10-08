"""
质数求解问题
"""
import math


def count_primes(n: int) -> list:
    """
    给定一个数n，返回[0, n]中所有质数的集合。
    :param n: 目标数
    :return: 质数列表
    """
    is_prime = [True for _ in range(n + 1)]
    is_prime[0], is_prime[1] = False, False  # 0和1不是质数

    """ 从2开始，遍历到sqrt(n)即可，凡是这个区间内倍数的数字都不可能是质数 """
    for i in range(2, math.ceil(math.sqrt(n))):
        """ j从i^2开始遍历即可，假设i=4，若从2开始计算会计算：2x4，3x4，但在i=2和i=3时已经计算过了，因此j只需要从4^2开始遍历即可 """
        j = i ** 2
        if is_prime[j]:
            while j <= n:
                is_prime[j] = False
                j += i

    res = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            res.append(i)

    return res


if __name__ == '__main__':
    print(count_primes(13))

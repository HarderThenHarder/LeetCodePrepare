"""
单调栈问题，只用来解决 Next Greater Element 问题。
"""


def get_next_greater_element(arr):
    """
    返回与arr相同维度的一维列表，列表中每一个元素代表arr中右边第一个比自身大的元素，若没有则返回-1.
    :param arr: 目标数组
    :return: 一维列表
    """
    stack, res = [], [0 for _ in range(len(arr))]

    # 从后往前开始遍历
    for i in range(len(arr)-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        tmp = -1 if not stack else stack[-1]
        res[i] = tmp
        stack.append(arr[i])
    return res


def get_next_greater_element_distance(arr):
    """
    返回与arr相同维度的一维列表，列表中每个元素是arr中右边第一个比自身大的元素与自身的距离，没有返回-1.
    :param arr: 目标数组
    :return: 一维列表
    """
    stack, res = [], [0 for _ in range(len(arr))]

    for i in range(len(arr)-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        dis = 0 if not stack else stack[-1] - i     # 直接通过元素索引做差得到距离
        res[i] = dis
        stack.append(i)                             # 栈中存放的是元素索引，而不再是元素值
    return res


def get_next_greater_element_in_circle_array(arr):
    """
    在一个循环数组中找到列表中右边第一个比自身大的元素。
    :param arr: 目标数组
    :return: 一维列表
    """
    stack, res, length = [], [0 for _ in range(len(arr))], len(arr)

    for i in range(2*len(arr)-1, -1, -1):               # 将arr乘以两倍，取i的时候取个模长
        while stack and stack[-1] <= arr[i%length]:
            stack.pop()
        tmp = -1 if not stack else stack[-1]
        res[i%length] = tmp
        stack.append(arr[i%length])
    return res


if __name__ == '__main__':
    print(get_next_greater_element([2, 1, 2, 4, 3]))
    print(get_next_greater_element_distance([73, 74, 75, 71, 69, 72, 76, 73]))
    print(get_next_greater_element_in_circle_array([2, 1, 2, 4, 3]))
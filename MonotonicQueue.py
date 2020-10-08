"""
单调队列问题，用于解决滑动窗口最大值问题。
"""


class MonotonicQueue:

    def __init__(self, queue):
        self.queue = queue

    def push(self, val):
        """
        压一个新的值入队列，将队列中所有比新值小的元素全弹出。
        :param val: 新插入值
        :return: None
        """
        while self.queue and self.queue[-1] <= val:
            self.queue.pop()
        self.queue.append(val)

    def pop(self, val):
        """
        弹出队头元素，当且仅当队头元素等于val时才弹出。
        :param val: 弹出队头的目标值
        :return: None
        """
        if self.queue and self.queue[0] == val:
            self.queue.pop(0)

    def max(self):
        """
        返回当前队列中最大值，即返回队头元素值。
        :return: value
        """
        if self.queue:
            return self.queue[0]


def max_slide_window(arr, k):
    """
    输入一个数组arr，窗口大小为k，输出窗口滑动中每次滑动的最大值。
    :param arr: 数组
    :param k: 窗口大小
    :return: 最大值列表
    """
    window = MonotonicQueue([])
    res = []
    for i in range(len(arr)):
        if i < k - 1:                   # 当队列里存到 k-1 个数的时候就开始走 else 分支
            window.push(arr[i])
        else:
            window.push(arr[i])         # 压入一个新数，此时队列已满 k 个数
            res.append(window.max())    # 拿出 k 个数中最大的数
            window.pop(arr[i-k+1])      # 弹出队头元素，i-k+1是arr中队头元素的索引
    return res


if __name__ == '__main__':
    print(max_slide_window([1, 3, -1, -3, 5, 3, 6, 7], 3))

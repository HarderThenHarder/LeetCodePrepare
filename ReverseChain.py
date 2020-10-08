"""
链表翻转问题：
    1. 普通链表翻转
    2. 按k个一组进行翻转
    3. 翻转链表中的一部分
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(head):
    """
    翻转链表，返回新链表头节点（原地算法，不申请额外空间）。
    :param head: 头节点
    :return: 新头节点
    """
    if not head:
        return None
    if not head.next:
        return head

    dummy, p = Node(-1), head
    # 头插法
    while p:
        tmp = dummy.next
        dummy.next = p
        p = p.next
        dummy.next.next = tmp

    return dummy.next


def reverse_k_chain(head, k):
    """
    按k个一组翻转链表，不够k个的一组不翻转。
    :param head: 头节点
    :param k: k个为一组
    :return: 新头节点
    """
    length, p, dummy = 0, head, Node(-1)
    while p:
        length += 1
        p = p.next

    # last存储的是链表最后一个节点，k个一组中用头插法，下一个k组需接在前一个k组之后
    p, last, start = head, None, dummy
    while length >= k:
        for i in range(k):
            if not i:
                last = p
            tmp = start.next
            start.next = p
            p = p.next
            start.next.next = tmp
        length -= k
        start = last

    if length:
        start.next = p

    return dummy.next


def reverse_between(head, m, n):
    """
    翻转链表中[m, n]中的部分。
    :param head: 头节点
    :param m: 起始点
    :param n: 终点
    :return: 新节点
    """
    p, pre = head, None
    # 将起点挪到m节点
    for i in range(m):
        # 记录m-1节点，为了连接后面的部分
        if i == m-1:
            pre = p
        p = p.next

    dummy, last = Node(-1), None
    # 将[m,n]部分做翻转
    for i in range(n-m+1):
        if not i:
            last = p
        tmp = dummy.next
        dummy.next = p
        p = p.next
        dummy.next.next = tmp

    # m-1节点连接到翻转部分的头节点
    pre.next = dummy.next
    # 将翻转部分的最后一个节点与原链表后半部分连接
    last.next = p

    return head


def build_chain(arr):
    head = Node(arr[0])
    p = head
    for i in range(1, len(arr)):
        p.next = Node(arr[i])
        p = p.next
    return head


def visit_chain(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print('None')


if __name__ == '__main__':
    head = build_chain([1, 2, 3, 4, 5])
    # reverse_head = reverse(head)
    # visit_chain(reverse_head)
    # r_k_head = reverse_k_chain(head, 2)
    # visit_chain(r_k_head)
    r_mn_head = reverse_between(head, 2, 3)
    visit_chain(r_mn_head)
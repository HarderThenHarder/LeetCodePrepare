"""
回溯法解题，回溯法框架：

def backtrack(path, choice):
    if (满足条件):
        res.append(path.copy())
        return
    for c in choice:
        path.append(c)
        choice.remove(c)
        backtrack(path, choice)
        path.remove(c)
        choice.insert(c)
"""


def generate_brackets(left, right, n, path, res):
    """
    给定输入n，代表n对括号，输出所有合法的括号组合。 如：n=3，res = ["((()))", "((()())", "(())()", "()(())", "()()()"]
    :param left: 当前括号组合中左括号的个数
    :param right: 当前括号组合中右括号的个数
    :param path: 当前括号组合
    :param res: 括号组合列表
    :return: None
    """
    if left < right or left > n or right > n:            # 组合中左括号数小于右括号数h，左/右括号数大于n，该组合不合法，直接返回。
        return
    if len(path) == 2 * n:
        res.append(path)
        return

    path += '('
    generate_brackets(left+1, right, n, path, res)
    path = path[:-1]

    path += ')'
    generate_brackets(left, right+1, n, path, res)
    path = path[:-1]


if __name__ == '__main__':
    res = []
    generate_brackets(0, 0, 3, "", res)
    print(res)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isBST(root: TreeNode, min_node, max_node) -> bool:
    """
    判断一个树是否为二叉搜索树。
    :param root: 根节点
    :param min_node: 最小值限制点
    :param max_node: 最大值限制点
    :return: 布尔值
    """
    if not root:
        return True

    if min_node and root.val < min_node.val:
        return False
    if max_node and root.val > max_node.val:
        return False

    """ 最关键的一步，root的左子树（并非左孩子）上所有节点值都必须小于当前root节点的值，所以传入左孩子的时候要限定max上限 """
    return isBST(root.left, min_node, root) and isBST(root.right, root, max_node)


def isInBST(root, target):
    """
    判断目标值是否在二叉搜索树内。
    :param root: 根节点
    :param target: 目标值
    :return: 布尔值
    """
    if not root:
        return False

    if root.val == target:
        return True
    elif root.val > target:
        return isInBST(root.left, target)
    else:
        return isInBST(root.right, target)


def addNumber(root, target):
    """
    将一个新的target值添加入二叉搜索树中。
    :param root: 根节点
    :param target: 目标值
    :return: 根节点
    """
    if not root:      # 新节点都插在树的最下层
        return TreeNode(target)

    if root.val > target:
        root.left = addNumber(root.left, target)
    if root.val < target:
        root.right = addNumber(root.right, target)

    return root


def deleteNumber(root, target):
    """
    删除二叉搜索树中的target值，删除比插入要复杂，在删除的过程中必须保证删除节点后BST的结构不被破坏，一共有以下3种情况：
    1. 待删除点既无左孩子也无右孩子 —— 直接删除
    2. 待删除点只有左孩子/右孩子 —— 将其右孩子/左孩子放到自身的位置即可
    3. 待删除点左右孩子均存在 —— 选择右子树中最小的节点放到自身位置即可
    :param root: 根节点
    :param target: 待删除值
    :return: 根节点
    """
    if not root:
        return

    if root.val == target:
        """ case 1 """
        if not root.left and not root.right:
            return None

        """ case 2 """
        if root.left and not root.right:
            return root.left
        if not root.left and root.right:
            return root.right

        """ case 3 """
        if root.left and root.right:
            min_node = get_min_node(root.right)
            root.val = min_node.val                               # 将当前节点值赋值为右子树最小值，等于把最小值节点移到当前节点
            root.right = deleteNumber(root.right, min_node.val)   # 将待删除值变为右子树最小值，等于删除了右子树的最小值节点

    elif root.val > target:
        root.left = deleteNumber(root.left, target)
    elif root.val < target:
        root.right = deleteNumber(root.right, target)

    return root


def get_min_node(root):
    while root.left:
        root = root.left
    return root


def lowest_common_ancestor(root, p, q):
    """
    寻找二叉树上两个树节点p, q最近的公共祖先。
    :param root: 根节点
    :param p: 目标节点1
    :param q: 目标节点2
    :return: root
    """
    if not root or root.val == p or root.val == q:      # 该结点等于两个目标节点中任意一个节点，则该节点就是最近的公共祖先
        return root

    left = lowest_common_ancestor(root.left, p, q)      # 判断该root结点的左子树中是否包含目标结点
    right = lowest_common_ancestor(root.right, p, q)    # 判断该root结点的右子树中是否包含目标结点

    if left and right:          # 若左右子树均包含目标结点，则代表左右子树一边包含一个目标结点，则该root一定是最近的公共祖先
        return root
    elif not left and right:    # 若两个目标结点都在右边，则返回右节点
        return right
    elif not right and left:    # 若两个目标节点都在左边，则返回左节点
        return left

    return None


def visitTree(root):
    if not root:
        return
    print(root.val)
    visitTree(root.left)
    visitTree(root.right)


if __name__ == '__main__':
    """
    构建如下所示的树:
           5
          / \ 
         2   6
        / \   \
       1   4   7
    """
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Lowest Common Ancestor: ", lowest_common_ancestor(root, 1, 4).val)

    print("Is BST: ", isBST(root, None, None))  # 判断是否为合法的二叉搜索树
    print("In BST: ", isInBST(root, 8))         # 判断目标值是否在二叉搜索树内

    r = addNumber(root, 3)          # 将3添加入二叉搜索树
    visitTree(r)                    # 查看新的树的结果

    r = deleteNumber(root, 2)       # 删除搜索树中值为2的节点
    visitTree(r)                    # 查看新的树的结果

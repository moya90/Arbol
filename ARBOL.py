class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
    return root

def in_order_traversal(root, result):
    if root:
        in_order_traversal(root.left, result)
        result.append(root.val)
        in_order_traversal(root.right, result)

def balance_tree(nodes):
    nodes.sort()
    return sorted_array_to_bst(nodes, 0, len(nodes) - 1)

def sorted_array_to_bst(nodes, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = TreeNode(nodes[mid])

    root.left = sorted_array_to_bst(nodes, start, mid - 1)
    root.right = sorted_array_to_bst(nodes, mid + 1, end)

    return root

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val, end=' ')
        print_tree(root.right)

if __name__ == "__main__":
    nodes = [10, 5, 15, 20]

    root = None
    for node in nodes:
        root = insert(root, node)

    print("Árbol binario desbalanceado:")
    print_tree(root)

    balanced_root = balance_tree(nodes)
    print("\nÁrbol binario balanceado:")
    print_tree(balanced_root)

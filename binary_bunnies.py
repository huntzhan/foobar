from math import factorial


class Node(object):

    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None
        self._size = None

    def add_child(self, other_node):
        if other_node.label > self.label:
            # "older ages to the left and younger to the right"
            target_node = 'left'
        else:
            target_node = 'right'

        if getattr(self, target_node) is None:
            setattr(self, target_node, other_node)
        else:
            getattr(self, target_node).add_child(other_node)

    @property
    def size(self):
        if self._size is None:
            self._size = 1
            self._size += 0 if self.left is None else self.left.size
            self._size += 0 if self.right is None else self.right.size
        return self._size

    def to_string(self):
        return '{0} ({1} {2})'.format(
            self.label,
            '' if self.left is None else self.left.to_string(),
            '' if self.right is None else self.right.to_string(),
        )


def count(node):
    if node is None or node.size == 1:
        return 1
    left_size = 0 if node.left is None else node.left.size
    right_size = 0 if node.right is None else node.right.size
    permutations = (factorial(left_size + right_size)
                    / (factorial(left_size) * factorial(right_size)))
    return permutations * count(node.left) * count(node.right)


def answer(seq):
    # 1. build a tree.
    root = Node(seq[0])
    for descendant in map(Node, seq[1:]):
        root.add_child(descendant)
    # 2. count.
    return count(root)

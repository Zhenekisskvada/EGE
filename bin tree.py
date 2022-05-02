class Node:
    def __init__(self, head, left, right, value):
        self.head = head
        self.left = left
        self.right = right
        self.value = value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_value(self, value):
        self.value = value


head = Node(None, None, None, 1)
left = Node(head, None, None, 2)
right = Node(head, None, None, 3)


head.set_left(left)
head.set_right(right)


left1 = Node(left, None, None, 4)
right1 = Node(left, None, None, 5)
left.set_left(left1)
left.set_right(right1)


left = Node(right1, None, None, 6)
right = Node(right1, None, None, 7)

right1.set_left(left)
right1.set_right(right)


def passing_tree(current):
    print(current.value)

    if current.left:
        passing_tree(current.left)

    if current.right:
        passing_tree(current.right)


passing_tree(head)

def passing_tree_row():

import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add(root, x):
    if root is None:
        return Node(x)

    cur = root

    while True:
        if x < cur.key:
            if cur.left is None:
                cur.left = Node(x)
                break
            cur = cur.left

        elif x > cur.key:
            if cur.right is None:
                cur.right = Node(x)
                break
            cur = cur.right

        else:
            break

    return root


def preorder(root, ans):
    if root is None:
        return

    ans.append(root.key)
    preorder(root.left, ans)
    preorder(root.right, ans)


def rotate_left(root, x):
    if root.key == x:
        b = root.right
        root.right = b.left
        b.left = root
        return b

    if x < root.key:
        root.left = rotate_left(root.left, x)
    else:
        root.right = rotate_left(root.right, x)

    return root


def rotate_right(root, x):
    if root.key == x:
        b = root.left
        root.left = b.right
        b.right = root
        return b

    if x < root.key:
        root.left = rotate_right(root.left, x)
    else:
        root.right = rotate_right(root.right, x)

    return root


def main():
    n = int(input())
    a = list(map(int, input().split()))

    root = None

    for x in a:
        root = add(root, x)

    m = int(input())

    for _ in range(m):
        command = input().split()
        x = int(command[1])

        if command[0] == "left":
            root = rotate_left(root, x)
        else:
            root = rotate_right(root, x)

        ans = []
        preorder(root, ans)
        print(*ans)


if __name__ == "__main__":
    main()
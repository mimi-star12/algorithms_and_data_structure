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


def exists(root, x):
    cur = root

    while cur is not None:
        if x == cur.key:
            return True
        if x < cur.key:
            cur = cur.left
        else:
            cur = cur.right

    return False


def delete(root, x):
    if root is None:
        return None

    if x < root.key:
        root.left = delete(root.left, x)
    elif x > root.key:
        root.right = delete(root.right, x)
    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        mn = root.right
        while mn.left is not None:
            mn = mn.left

        root.key = mn.key
        root.right = delete(root.right, mn.key)

    return root


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def preorder(root, ans):
    if root is None:
        return

    ans.append(root.key)
    preorder(root.left, ans)
    preorder(root.right, ans)


def main():
    q = int(input())
    root = None

    for _ in range(q):
        s = input().split()

        if s[0] == "add":
            root = add(root, int(s[1]))
        elif s[0] == "del":
            root = delete(root, int(s[1]))
        elif s[0] == "exists":
            if exists(root, int(s[1])):
                print("YES")
            else:
                print("NO")
        elif s[0] == "height":
            print(height(root))
        elif s[0] == "print":
            ans = []
            preorder(root, ans)

            if len(ans) > 0:
                print(*ans)
            else:
                print("Empty")


if __name__ == "__main__":
    main()
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(root):
    if root is None:
        return 0
    return root.height


def fix_height(root):
    root.height = 1 + max(
        get_height(root.left),
        get_height(root.right)
    )


def rotate_left(root):
    b = root.right
    root.right = b.left
    b.left = root

    fix_height(root)
    fix_height(b)

    return b


def rotate_right(root):
    b = root.left
    root.left = b.right
    b.right = root

    fix_height(root)
    fix_height(b)

    return b


def balance(root):
    fix_height(root)

    k = get_height(root.right) - get_height(root.left)

    if k == 2:
        right_k = (
            get_height(root.right.right)
            - get_height(root.right.left)
        )

        if right_k < 0:
            root.right = rotate_right(root.right)

        return rotate_left(root)

    if k == -2:
        left_k = (
            get_height(root.left.right)
            - get_height(root.left.left)
        )

        if left_k > 0:
            root.left = rotate_left(root.left)

        return rotate_right(root)

    return root


def add(root, x):
    if root is None:
        return Node(x)

    if x < root.key:
        root.left = add(root.left, x)
    elif x > root.key:
        root.right = add(root.right, x)
    else:
        return root

    return balance(root)


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
        command = input().split()

        if command[0] == "add":
            root = add(root, int(command[1]))

        elif command[0] == "exists":
            if exists(root, int(command[1])):
                print("YES")
            else:
                print("NO")

        elif command[0] == "root":
            if root is None:
                print("Empty")
            else:
                print(root.key)

        elif command[0] == "height":
            print(get_height(root))

        elif command[0] == "print":
            ans = []
            preorder(root, ans)

            if len(ans) == 0:
                print("Empty")
            else:
                print(*ans)


if __name__ == "__main__":
    main()
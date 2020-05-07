def solution(h,q):
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    def mkdummytree(arr, root, i, n):
        if i < n:
            temp = Node(arr[i])
            root = temp
            root.left = mkdummytree(arr, root.left,
                                         2 * i + 1, n)

            root.right = mkdummytree(arr, root.right,
                                          2 * i + 2, n)
        return root

    def postorderlabel(root, ar, i):
        if root:
            i = postorderlabel(root.left, ar, i)
            i = postorderlabel(root.right, ar, i)
            root.val = ar[i]
            return i + 1
        else: return i

    def searchparent(root, key):
        if root is None:
            return None
        p = None
        while root is not None:
            left = root.left
            if left is None:
                break
            if key == root.val:
                break
            elif key <= left.val:
                p = root
                root = root.left
            elif key > left.val:
                p = root
                root = root.right
        return p

    ## Driver Code:
    ar = [x for x in range(1, 2 ** h)]
    n=len(ar)
    root=None
    root=mkdummytree(ar, root, 0, n)
    x=postorderlabel(root,ar,0)
    ans=[]
    for k in q:
        s = searchparent(root, k)
        if s:
            ans.append(s.val)
        else:
            ans.append(-1)
    return ans
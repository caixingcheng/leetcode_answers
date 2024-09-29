# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        inorder(ans,root)
        return ans
def inorder(ans,root):
    if not root:
        return
    inorder(ans,root.left)
    ans.append(root.val)
    inorder(ans,root.right)

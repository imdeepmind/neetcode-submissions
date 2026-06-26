# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def check(head):
            nonlocal is_balanced

            if not is_balanced:
                return 0

            if not head:
                return 0
            
            left_height = check(head.left)
            right_height = check(head.right)

            if abs(left_height - right_height) > 1:
                is_balanced = False
            
            return 1 + max(left_height, right_height)
        
        check(root)

        return is_balanced
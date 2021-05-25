# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return 0
        
        return self.pathSum(root, targetSum, 0)
    
    def pathSum(self, root, target, targetSum):
        if root.left == None and root.right != None:
            return self.pathSum(root.right, target, targetSum+root.val)
            
        if root.left != None and root.right == None:
            return self.pathSum(root.left, target, root.val+targetSum)
        
        if root.left == None and root.right == None:
            if targetSum + root.val == target:
                return True
            else:
                return False
        
        return self.pathSum(root.left, target, root.val+targetSum) or self.pathSum(root.right, target, targetSum+root.val)
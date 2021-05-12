class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def postorderTraversal(root):
  answer = []
  if root != None:
    stack1 = [root]
    stack2 = []

    while len(stack1) > 0:
      removed = stack1.pop()
      answer.append(removed.val)
      stack2.append(removed)

      if removed.left != None:
        stack1.append(removed.left)
      if removed.right != None:
        stack1.append(removed.right)

  return answer[::-1]


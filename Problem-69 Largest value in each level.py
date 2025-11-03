# 515. Find Largest Value in Each Tree Row

# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result
        
        q = deque()
        q.appendleft(root)

        while q:
            size = len(q)
            maxNum = -inf
            for i in range(size):
                curr = q.pop()
                maxNum = max([maxNum,curr.val])

                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    q.appendleft(curr.right)
            result.append(maxNum)
        return result

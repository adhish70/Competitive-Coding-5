# 515. Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS

# Logic: Perform level order traversal. Maintain the max for each level. 
# After the level is traversed, add the max to the result.

# Time Complexiety: O(n)
# Space Complexiety: O(n)

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = list()
        q.append(root)
        size = 0
        res = list()
        
        while q:
            size = len(q)
            cur_max = -inf
            
            for i in range(size):
                node = q.pop(0)
                cur_max = max(cur_max, node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(cur_max)
        return res

# DFS

# Time Complexiety: O(n)
# Space Complexiety: O(n)
class Solution:            
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [(root,0)]
        res = []
        
        while stack:
            node, lvl = stack.pop()
            
            if node:
                if len(res) == lvl:
                    res.append(node.val)
                else:
                    res[lvl] = max(res[lvl],node.val)
                
                stack.append((node.right,lvl+1))
                stack.append((node.left,lvl+1))        
        return res

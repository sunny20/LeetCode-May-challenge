# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = [root]
        while level != []:
            child_level = []
            child_parent_dic = {} 
            for i in range(len(level)):
                node = level.pop(0)
                if node.left:
                        child_level.append(node.left)
                        child_parent_dic[node.left.val] = node.val
                if node.right:
                        child_level.append(node.right)
                        child_parent_dic[node.right.val] = node.val
                child_val = [i.val for i in child_level]
                if x in child_val and y in child_val:
                    if child_parent_dic[x] != child_parent_dic[y]:
                        return True
            level = child_level
        return False
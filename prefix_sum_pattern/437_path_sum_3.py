# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        mapper = {0: 1}
        if not root:
            return 0
        def dfs(node: TreeNode, result: int, curr_sum: int) -> int:
            # add to curr sum the current node
            # store the curr_sum in hash map
            curr_sum = curr_sum + node.val
            diff = curr_sum - targetSum
            # This needs to be removed 
            # from curr sum to get the target sum
            # let's check if it is there in hashmap
            # if it is add all those possibilities to the result
            result = result + mapper.get(diff, 0)
            mapper[curr_sum] = mapper.get(curr_sum, 0) + 1
            if node.left:
                result = dfs(node.left, result, curr_sum)
            if node.right:
                result = dfs(node.right, result, curr_sum)    
            
            # Need to pop the current value from the hashmap
            # Need to subtract the current sum away as well
            # No need to subtract cause of recursion
            mapper[curr_sum] -= 1
            return result

        return dfs(root, 0, 0)

        
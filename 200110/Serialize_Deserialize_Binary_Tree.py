# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        queue = [root]
        ans = []
        while queue:
            cur_node = queue.pop(0)
            if cur_node:
                queue.append(cur_node.left)
                queue.append(cur_node.right)
            ans.append(str(cur_node.val) if cur_node else '#')
        return ','.join(ans)
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        queue = []
        if data[0] != '#':
            root = TreeNode(int(data[0]))
            queue.append(root)
        else:
            return None
        
        idx = 1
        while queue:
            cur_node = queue.pop(0)
            if data[idx] != '#':
                cur_node.left = TreeNode(int(data[idx]))
                queue.append(cur_node.left)
            else:
                cur_node.left = None
                
            idx += 1
            if data[idx] != '#':
                cur_node.right = TreeNode(int(data[idx]))
                queue.append(cur_node.right)
            else:
                cur_node.right = None
                
            idx += 1
            
        return root
        
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))




'''
Simple and Brute DFS solution:

class Solution:

    def serialize(self, root):
        if not root: return ['#']
        return [str(root.val)] + self.serialize(root.left) + self.serialize(root.right)
    
    def deserialize(self, data):
        elem = data.pop(0)
        if elem == '#': return None 
        root = TreeNode(int(elem))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root

        
'''
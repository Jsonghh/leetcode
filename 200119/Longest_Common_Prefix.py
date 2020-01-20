class TrieNode:
    def __init__(self,):
        self.children = {}
        self.if_stop = False
        

class Trie:
    def __init__(self,):
        self.root = TrieNode()
        
        
    def insert(self, word):
        node = self.root
        
        for c in word:
            if node.if_stop:
                return
            
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            
        node.if_stop = True
            

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        trie = Trie()
        
        for word in strs:
            if not word:
                return ''
            trie.insert(word)
            
        node, ans = trie.root, ''
        
        while True:
            if len(node.children) > 1:
                break
            
            if node.if_stop:
                break
                
            next_letter = list(node.children.keys())[0]
            ans += next_letter
            node = node.children[next_letter]
            
        return ans
        
            
        
            
        
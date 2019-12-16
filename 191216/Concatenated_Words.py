class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        
    
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return node
        return node
    
    
    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word
    
    
    def startsWith(self, prefix):
        return self.find(prefix) is not None
        
    

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            if self.helper(word, 0, trie, 0):
                ans.append(word)
        return ans
    
    
    def helper(self, word, idx, trie, wcnt):
        if idx == len(word):
            return wcnt >= 2
        for i in range(idx, len(word)):
            pre = word[idx : i + 1]
            if trie.search(pre):
                wcnt += 1
                if self.helper(word, i + 1, trie, wcnt):
                    return True
                wcnt -= 1
        return False
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ans = []
#         for word in words:
#             if not word:
#                 continue
#             word_set = set(words)
#             word_set.remove(word)
#             if self.helper(word, word_set):
#                 ans.append(word)
#             word_set.add(word)
#         return ans
    
    
    
#     def helper(self, word, word_set):
#         if word in word_set:
#             return True
#         for sep in range(1, len(word)):
#             pre, suff = word[:sep], word[sep:]
#             if pre in word_set and self.helper(suff, word_set):
#                 return True
#         return False
        
        
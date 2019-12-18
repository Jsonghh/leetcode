class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        return self.helper(self.root, word, 0)
        
        
    def helper(self, node, word, idx):
        if not node:
            return False
        if idx == len(word):
            return node.is_word
        
        c = word[idx]
        if c != '.':
            return self.helper(node.children.get(c), word, idx + 1)
        else:
            for nn in node.children.values():
                if self.helper(nn, word, idx + 1):
                    return True
            else:
                return False
            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
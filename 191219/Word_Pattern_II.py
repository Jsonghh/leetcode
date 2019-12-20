class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        return self.helper(pattern, str, {}, set())
    
    
    def helper(self, ptt, str, mapping, used):
        if not ptt:
            return not str
        
        char = ptt[0]
        if char in mapping:
            word = mapping[char]
            if not str.startswith(word):
                return False
            return self.helper(ptt[1:], str[len(word):], mapping, used)
        
        for i in range(len(str)):
            word = str[:i + 1]
            if word in used:
                continue
            mapping[char] = word
            used.add(word)
            if self.helper(ptt[1:], str[i + 1:], mapping, used):
                return True
            del mapping[char]
            used.remove(word)
        return False
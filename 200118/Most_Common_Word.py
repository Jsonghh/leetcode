from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph, banned) :
        d = defaultdict(int)
        par = []
        
        for char in paragraph:
            if not char.isalpha():
                paragraph = paragraph.replace(char, ' ')
                
        par = paragraph.lower().split()
        
        for word in par:
            if word in banned:
                continue
            d[word] += 1
            
        frequency = max(d.values())
        
        for word in d:
            if d[word] == frequency:
                return word
            
        return ''
        
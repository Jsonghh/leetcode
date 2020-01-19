from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        parent = defaultdict(list)

        for word in strs:
            p = ''.join(sorted(word))
            parent[p].append(word)
            
        ans = [anagrams for anagrams in parent.values()]
        
        return ans
        
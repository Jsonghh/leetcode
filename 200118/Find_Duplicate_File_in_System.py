
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for path in paths:
            dirc, *files = path.split(' ')
            for file in files:
                file_name, content = file.split('(')
                d[content].append(dirc + '/' + file_name)
                
        ans = [v for v in d.values() if len(v) > 1]
        return ans
            
        
        
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Write your code here
        # use flog to utilize zigzag 
        result = [[] for _ in range(numRows)]
        print(len(s))
        res = ""
        
        i = 0
        zigzag = 0
        while i < len(s):
            if zigzag == 0:
                for j in range(len(result)):
                    if i < len(s):
                        result[j].append(s[i])
                        i += 1   
                zigzag = 1
                
            else:
                for j in range(len(result) - 2, 0, -1):
                    if i < len(s):
                        result[j].append(s[i])
                        i += 1
                zigzag = 0
        
        for words in result:
            for word in words:
                res += word
        
        return res
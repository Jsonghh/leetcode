'''
https://leetcode.com/problems/text-justification/discuss/478806/python-95-easy-to-follow-detailed-comments
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        lines, line, len_sofar = [], [], 0
        
        for word in words:
            if len(word) + len_sofar > maxWidth:
                lines.append(line[:])
                line, len_sofar = [], 0
                
            line.append(word)
            len_sofar += len(word) + 1 
            
        lines.append(line)
            
        for line_ in lines[:-1]:
            full_line = ''
            tot_space = maxWidth - sum([len(s) for s in line_])
            space_slot = len(line_) - 1 if len(line_) > 1 else 1
            
            if len(line_) == 1:
                full_line = line_[0].ljust(maxWidth, ' ')
            else:
                for i in range(len(line_) - 1):
                    full_line += line_[i] + ' ' * (tot_space // space_slot + 1 \
                                if i < tot_space % space_slot  else  tot_space // space_slot)
                full_line += line_[-1]
                
            ans.append(full_line)
            
        ans.append(' '.join(lines[-1]).ljust(maxWidth, ' '))
        
        return ans
        
        
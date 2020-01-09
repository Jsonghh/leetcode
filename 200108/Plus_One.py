class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        last = digits[-1] + 1
        if last < 10:
            digits[-1] += 1
            return digits
            
        carry = 1    
        for num in digits[::-1]:
            if num + carry == 10:
                ans.append(0)
            else:
                ans.append(num + carry)
                carry = 0
        if carry:
            ans.append(1)
        return ans[::-1]
                
        


'''
Brainless Approach

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = ''.join(map(str,digits))
        digits = int(digits)
        digits += 1
        digits = list(str(digits))
        return digits
'''
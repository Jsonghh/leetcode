class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = []
        if x < 0:
            return False
        
        while x:
            x, rem = divmod(x, 10)
            x_list.append(rem)
            
        return x_list == x_list[::-1]



        # x = str(x)
        # return x == x[::-1]
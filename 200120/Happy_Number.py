class Solution:
    def isHappy(self, n: int) -> bool:
        # tortoise, hare = n, self.get_next(n)
        # while hare != 1 and tortoise != hare:
        #     tortoise, hare = self.get_next(tortoise), self.get_next(self.get_next(hare))
        # return hare == 1
        
        
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}
        while n != 1 and n not in cycle_members:
            n = self.get_next(n)

        return n == 1
        
    def get_next(self, n):
        new_num = 0
        while n > 0:
            quo, rem = divmod(n, 10)
            new_num += rem ** 2
            n = quo
            
        return new_num
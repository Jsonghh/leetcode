# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        possible_c = 0
        for i in range(1, n):
            if knows(possible_c, i):
                possible_c = i
        
        for i in range(n):
            if i != possible_c and knows(possible_c, i):
                return -1
            if i != possible_c and not knows(i, possible_c):
                return -1
        return possible_c
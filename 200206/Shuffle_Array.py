import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        
        return self.original
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        if not self.original:
            return []
        
        permutation = list(self.original)
        taken = set()
        
        for i in range(len(permutation)):
            p = random.randint(0, len(permutation) - 1)
            permutation[i], permutation[p] = permutation[p], permutation[i]
        
        return permutation
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()



'''
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.permutations = []
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        
        return self.original
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        
        self.helper([], set())
        return random.choice(self.permutations)
    
    
    def helper(self, cur, visited):
        if len(cur) == len(self.original):
            self.permutations.append(cur[:])
            return
            
        for i in range(len(self.original)):
            if i in visited:
                continue
            cur.append(self.original[i])
            visited.add(i)
            self.helper(cur, visited)
            cur.pop()
            visited.remove(i)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
'''
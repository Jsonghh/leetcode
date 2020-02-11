class Solution:
    def lastRemaining(self, n: int) -> int:
        # idea from: https://leetcode.com/problems/elimination-game/discuss/87119/JAVA:-Easiest-solution-O(logN)-with-explanation

        # the value distance between each remaining element in the list
        step = 1
        # the first (counting from left) remaining element
        head = 1
        # the number of remaining element
        remains = n
        # record the current direction
        left = True

        while remains > 1:
            # two cases where head need to advance to the next remaining element
            # because current element will be eliminated
            # 1) we move from left to right
            # 2) we move from right to left, and there are odd number of remaining element
            if left or (remains & 1):
                head += step

            # after each round of elimination, the distance between every pair
            # of remaining elements will double
            step *= 2
            # the number of remaining elemnet will halve
            remains //= 2
            # change direction
            left = not left

        return head
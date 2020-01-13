class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 0
        sum_, idx = 0, 0
        
        while len(arr) >= 2:
            father = float('inf')
            for i in range(1, len(arr)):
                if arr[i] * arr[i - 1] < father:
                    father = arr[i] * arr[i - 1]
                    idx = i
            sum_ += father

    #         arr[idx], arr[idx - 1] comparison
            if arr[idx - 1] < arr[idx]:
                arr = arr[:idx - 1] + arr[idx:]
            else:
                arr = arr[:idx] + arr[idx + 1:]
        return sum_



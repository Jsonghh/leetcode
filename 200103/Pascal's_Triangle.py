class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            tmp_list = [1] * i
            if i < 3:
                ans.append(tmp_list)
                continue
            last_list = ans[-1]
            for k in range(1, len(tmp_list) - 1):
                tmp_list[k] = last_list[k] + last_list[k - 1]
            ans.append(tmp_list)
        return ans
                
        
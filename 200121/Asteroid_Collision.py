class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if not ans or a > 0 or ans[-1] < 0:
                ans.append(a)
                
            else:
                if_add_a = True
                while ans and a < 0 < ans[-1]:
                    if ans[-1] < -a:
                        ans.pop()
                        continue
                    elif ans[-1] == -a:
                        ans.pop()
                        if_add_a = False
                        break
                    else:
                        if_add_a = False
                        break
                if if_add_a:    
                    ans.append(a)
        return ans
                    
                
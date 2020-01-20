class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        while b:
            ans = a ^ b
            car = (a & b) << 1
            a, b = ans, car
            
        return bin(a)[2:]
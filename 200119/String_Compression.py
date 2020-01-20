class Solution:
    def compress(self, chars: List[str]) -> int:
        newchar_idx, write_idx = 0, 0
        
        for read_idx, c in enumerate(chars):
            if read_idx == len(chars) - 1 or chars[read_idx + 1] != c:
                chars[write_idx] = chars[newchar_idx]
                write_idx += 1
                
                if read_idx > newchar_idx:
                    for digit in str(read_idx - newchar_idx + 1):
                        chars[write_idx] = digit
                        write_idx += 1
                        
                newchar_idx = read_idx + 1
                
        return write_idx
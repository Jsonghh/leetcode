class Solution:
    def simplifyPath(self, path: str) -> str:
        path_split, stack = path.split('/'), []
        
        for p in path_split:
            if not p or p == '.':
                continue
                
            if p == '..':
                if stack:
                    stack.pop()
                
            else:
                stack.append(p)
                
        if not stack:
            return '/'
        
        return '/' + '/'.join(stack)
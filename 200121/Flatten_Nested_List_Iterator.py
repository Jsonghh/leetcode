# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.next_element = None
        self.stack = nestedList[::-1]
        
    
    def next(self) -> int:
        return self.next_element
        
    
    def hasNext(self) -> bool:
        
        while self.stack:
            cur = self.stack.pop()
            if cur.isInteger():
                self.next_element = cur.getInteger()
                return True
            else:
                cur_list = cur.getList()
                while cur_list:
                    self.stack.append(cur_list.pop())
        return False
            
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
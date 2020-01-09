
class MyCalendar:
    def __init__(self):
        self.events = []
        
    def book(self, start: int, end: int) -> bool:
        occupied = False
        start_event, end_event = (start, 1), (end, 0)
        self.events.append(start_event)
        self.events.append(end_event)
        self.events.sort()
        for time, status in self.events:
            if status == 0:
                occupied = False
                
            elif occupied:
                self.events.remove(start_event)
                self.events.remove(end_event)
                return False
            else:
                occupied = True
        return True
        

'''
Bisect in Python

https://www.jiuzhang.com/solution/my-calendar-i/#tag-other-lang-python
'''
            
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



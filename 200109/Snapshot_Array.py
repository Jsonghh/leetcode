from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.array = defaultdict(int)
        self.snap_id = -1
        self.snapshots = []
        self.length = length

    def set(self, index: int, val: int) -> None:
        if index >= self.length:
            return
        self.array[index] = val
        

    def snap(self) -> int:
        self.snapshots.append(self.array.copy())
        self.snap_id += 1
        
        return self.snap_id
        

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
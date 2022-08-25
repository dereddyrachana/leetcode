class SnapshotArray:

    def __init__(self, length: int):
        self.snap_shots = []
        self.snaps = {}
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.snaps[index] = val

    def snap(self) -> int:

        self.snap_shots.append(self.snaps.copy())
        self.snap_id += 1
    
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
            if index in self.snap_shots[snap_id]:
                return self.snap_shots[snap_id][index]
            else:
                return 0
# class SnapshotArray:

#     def __init__(self, length: int):
#         self.d_snap = {}
#         self.snap_id = 0
#         self.array = [0] * length
        
#     def set(self, index: int, val: int) -> None:
#         self.array[index] = val

#     def snap(self) -> int:
#         self.d_snap[self.snap_id] = tuple(self.array)
#         self.snap_id += 1
#         return self.snap_id -1

#     def get(self, index: int, snap_id: int) -> int:
#         if index in self.d_snap[snap_id]:
#             print(self.d_snap,index)
#             return self.d_snap[snap_id][index]
#         else:
#             return 0


# # Your SnapshotArray object will be instantiated and called as such:
# # obj = SnapshotArray(length)
# # obj.set(index,val)
# # param_2 = obj.snap()
# # param_3 = obj.get(index,snap_id)
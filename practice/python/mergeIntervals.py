from typing import List

class Solution:
    def merge2item(self, i1: List[int], i2: List[int]) -> List[List[int]]:
        if i1[1] < i2[0]:
            return [i1,i2]
        if i1[1] >= i2[0]:
            start = min(i1[0],i2[0])
            end = max(i1[1],i2[1])
            return [[start,end]]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        merged = self.merge2item(intervals[0], intervals[1])
        if len(intervals) == 2:
            return merged
        
        # merged
        for i in range(2, len(intervals),1):
           if len(merged) > 1:
               merged = self.merge(merged, intervals[i])
           else:
               merged = self.merge2item(merged[0], intervals[i+1])
        # overlapping check, no overlapping
        return merged
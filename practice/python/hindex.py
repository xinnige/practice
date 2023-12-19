from typing import List

class Solution:
        
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        
        citations = sorted(citations)
        hidx = 0
        size = len(citations)
        for i in range(size):
            idx = min(citations[i], size-i)
            if idx >= hidx:
                hidx = idx
            else:
                break
            
        return hidx

if __name__ == "__main__":
    sol = Solution()
    # print(sol.hIndex([3,1,2,3]))
    # print(sol.hIndex([1,2,3,3]))
    # print(sol.hIndex([1,1]))
    print(sol.hIndex([3,0,6,1,5]))
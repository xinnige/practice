from typing import List 

class Solution:
    def check_tailing(self, input:str, i :int)-> bool:
        # check tailing
        while i < len(input):
            if input[i] <= 'Z':
                return False
            i+=1
        return True
    
    def match(self, input:str, pattern:str, i:int,j:int) -> bool:
        if j == len(pattern):
            return self.check_tailing(input, i)
        if i == len(input):
            return j == len(pattern)
        if input[i] == pattern[j]:
            return self.match(input, pattern, i+1, j+1)
        elif input[i] > 'Z':
            return self.match(input,pattern, i+1, j)
        else:
            return False

    def camelMatch(self, query:List[str], pattern:str) -> List[bool]:
        result = [False]*len(query)
        for i in range(len(query)):
            result[i] = self.match(query[i], pattern,0,0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FB"))
    print(sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FoBa"))
    print(sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FoBaT"))
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        calstack = []
        for t in tokens:
            if t in ["+","-","*","/"]:
                num2 = calstack.pop()
                num1 = calstack.pop()
                calstack.append(self.calculate(t,num1,num2))
            else:
                calstack.append(int(t))
        return calstack[0]
    
    
    def calculate(self, token, num1, num2):
        if token == "+":
            return num1+num2
        if token == "-":
            return num1-num2
        if token == "*":
            return num1*num2
        if token == "/":
            return int(float(num1)/float(num2))
    


if __name__=='__main__':
     sol = Solution()
     print sol.evalRPN(["18"])
     print sol.evalRPN(["3","-4","+"])
     print sol.evalRPN(["2", "1", "+", "3", "*"])
     print sol.evalRPN(["4", "13", "5", "/", "+"])
     print sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

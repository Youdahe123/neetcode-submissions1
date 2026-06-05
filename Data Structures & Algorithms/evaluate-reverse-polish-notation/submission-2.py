class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num == "+":
                a,b = stack.pop(),stack.pop()
                stack.append(a + b)
            elif num == "-":
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif num == '*':
                a,b = stack.pop(),stack.pop()
                stack.append(a * b)
            elif num == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(num))
        return stack[0]
        
            
                
             

        
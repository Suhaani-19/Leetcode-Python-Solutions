class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until matching '(' is found
                sub = []
                while stack and stack[-1] != '(':
                    sub.append(stack.pop())
                
                # Pop the '('
                stack.pop()
                
                # Push the reversed substring back onto the stack
                stack.extend(sub)
            else:
                stack.append(char)
                
        return "".join(stack)
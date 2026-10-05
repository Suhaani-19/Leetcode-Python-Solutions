class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Base score level
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # max(2 * v, 1) handles () -> 1 and (A) -> 2 * A
                stack[-1] += max(2 * v, 1)
                
        return stack[0]
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # Initialize stack with -1 as a base boundary for valid substring calculations
        stack = [-1]

        for i, char in enumerate(s):
            if char == '(':
                # Push index of '(' onto stack
                stack.append(i)
            else:
                # Pop previous index on encountering ')'
                stack.pop()
                if not stack:
                    # If stack is empty, push current index as new boundary
                    stack.append(i)
                else:
                    # Calculate current valid length
                    max_len = max(max_len, i - stack[-1])

        return max_len
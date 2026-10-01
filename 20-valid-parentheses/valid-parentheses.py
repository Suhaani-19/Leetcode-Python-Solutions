class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check: odd length strings can never be balanced
        if len(s) % 2 != 0:
            return False

        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element if stack is not empty; otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the mapping matches
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push to stack
                stack.append(char)

        # If stack is empty, all opening brackets were properly closed
        return not stack
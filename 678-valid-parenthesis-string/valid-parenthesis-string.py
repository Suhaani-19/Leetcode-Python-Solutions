class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # Minimum possible open parentheses count
        high = 0  # Maximum possible open parentheses count

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            elif char == '*':
                low -= 1   # Treat '*' as ')'
                high += 1  # Treat '*' as '('

            # We can't have negative minimum open brackets
            if low < 0:
                low = 0

            # Too many closing brackets, invalid string
            if high < 0:
                return False

        # Valid if minimum required open count is 0
        return low == 0
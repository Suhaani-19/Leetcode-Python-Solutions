from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        queue = deque([s])
        visited = {s}
        found = False
        result = []

        while queue:
            curr = queue.popleft()

            if is_valid(curr):
                result.append(curr)
                found = True

            # If we found valid string(s) at the current level of removal, 
            # stop generating deeper levels.
            if found:
                continue

            # Generate all possible next states by removing one parenthesis
            for i in range(len(curr)):
                if curr[i] not in ('(', ')'):
                    continue
                nxt = curr[:i] + curr[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result
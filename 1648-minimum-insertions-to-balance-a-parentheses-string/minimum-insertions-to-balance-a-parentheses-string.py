class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:  # s[i] == ')'
                # Check if we have a pair of consecutive '))'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Missing one ')', so insert it
                    insertions += 1
                    i += 1
                
                # Match with an open '(' if available
                if open_count > 0:
                    open_count -= 1
                else:
                    # Missing an open '(', so insert it
                    insertions += 1
                    
        # Every unmatched '(' requires two ')'s
        insertions += open_count * 2
        return insertions
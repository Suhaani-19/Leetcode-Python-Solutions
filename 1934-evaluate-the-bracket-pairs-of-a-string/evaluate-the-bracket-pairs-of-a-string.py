class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge array to a hash map for O(1) lookups
        k_map = dict(knowledge)
        
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # Find the corresponding closing bracket
                j = s.find(')', i + 1)
                # Extract the key inside brackets
                key = s[i + 1:j]
                # Look up key; fallback to '?' if not found
                result.append(k_map.get(key, '?'))
                # Advance pointer to after the closing bracket
                i = j + 1
            else:
                result.append(s[i])
                i += 1
                
        return "".join(result)
class Solution:

  def minOperations(self, s: str) -> int:
    if s == "".join(sorted(s)):
      return 0
    if len(s) == 2:
      return -1

    min_char = min(s)
    max_char = max(s)

    # Check if 1 operation is enough
    # 1. min_char is at the start (proper prefix/suffix logic)
    # 2. max_char is at the end
    if s[0] == min_char or s[-1] == max_char:
      return 1

    # Check if 3 operations are needed
    if s.count(max_char) == 1 and s[0] == max_char and s.count(min_char) == 1 and s[-1] == min_char:
      return 3

    return 2
class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        for idx, char in enumerate(s, 1):
            # 'a' = 26, 'b' = 25, ..., 'z' = 1
            rev_alphabet_idx = 26 - (ord(char) - ord('a'))
            total_sum += rev_alphabet_idx * idx
        return total_sum
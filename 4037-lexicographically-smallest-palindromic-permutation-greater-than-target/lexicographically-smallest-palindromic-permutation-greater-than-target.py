from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odd_chars = [c for c in cnt if cnt[c] % 2 == 1]
        if len(odd_chars) > 1:
            return ""  # no palindrome permutation of s exists at all

        mid_char = odd_chars[0] if odd_chars else None
        half_cnt = Counter({c: cnt[c] // 2 for c in cnt if cnt[c] // 2 > 0})
        m = n // 2

        T1 = target[:m]
        if n % 2 == 1:
            Tmid, T2 = target[m], target[m + 1:]
        else:
            Tmid, T2 = None, target[m:]

        # --- Case B: H == T1 exactly ---
        if Counter(T1) == half_cnt:
            rev_T1 = T1[::-1]
            if n % 2 == 1:
                if mid_char > Tmid:
                    case_b_valid = True
                elif mid_char < Tmid:
                    case_b_valid = False
                else:
                    case_b_valid = rev_T1 > T2
            else:
                case_b_valid = rev_T1 > T2
            if case_b_valid:
                return T1 + (mid_char or "") + rev_T1

        # --- Case A: smallest H strictly greater than T1 ---
        cur = Counter(half_cnt)
        prefix_states = [Counter(cur)]
        feasible = True
        for i in range(m):
            if feasible and cur[T1[i]] > 0:
                cur[T1[i]] -= 1
                prefix_states.append(Counter(cur))
            else:
                feasible = False
                prefix_states.append(None)

        for p in range(m - 1, -1, -1):
            state = prefix_states[p]
            if state is None:
                continue
            target_char = T1[p]
            chosen = None
            for code in range(ord(target_char) + 1, ord('z') + 1):
                c = chr(code)
                if state.get(c, 0) > 0:
                    chosen = c
                    break
            if chosen is not None:
                new_state = Counter(state)
                new_state[chosen] -= 1
                suffix = "".join(
                    chr(code) * new_state.get(chr(code), 0)
                    for code in range(ord('a'), ord('z') + 1)
                )
                H = T1[:p] + chosen + suffix
                return H + (mid_char or "") + H[::-1]

        return ""
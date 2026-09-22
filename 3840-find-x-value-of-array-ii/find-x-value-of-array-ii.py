class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        # tree_cnt[node][r] stores the number of prefixes in node's range 
        # whose product modulo k is r
        self.tree_cnt = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 1, 0, self.n - 1)

    def build(self, nums, node, start, end):
        if start == end:
            val = nums[start] % self.k
            self.tree_prod[node] = val
            self.tree_cnt[node][val] = 1
            return
        
        mid = (start + end) // 2
        self.build(nums, 2 * node, start, mid)
        self.build(nums, 2 * node + 1, mid + 1, end)
        self.merge(node)

    def merge(self, node):
        left, right = 2 * node, 2 * node + 1
        self.tree_prod[node] = (self.tree_prod[left] * self.tree_prod[right]) % self.k
        
        # Merge counts:
        # Left child prefixes contribute directly
        for r in range(self.k):
            self.tree_cnt[node][r] = self.tree_cnt[left][r]
            
        # Right child prefixes are multiplied by the total product of the left child
        left_p = self.tree_prod[left]
        for r in range(self.k):
            new_r = (left_p * r) % self.k
            self.tree_cnt[node][new_r] += self.tree_cnt[right][r]

    def update(self, node, start, end, idx, val):
        if start == end:
            v = val % self.k
            self.tree_prod[node] = v
            for r in range(self.k):
                self.tree_cnt[node][r] = 0
            self.tree_cnt[node][v] = 1
            return
        
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.merge(node)

    def query(self, node, start, end, ql, qr):
        # Returns (product_mod_k, count_array) for the range [ql, qr]
        if ql <= start and end <= qr:
            return self.tree_prod[node], self.tree_cnt[node]
        
        mid = (start + end) // 2
        if qr <= mid:
            return self.query(2 * node, start, mid, ql, qr)
        if ql > mid:
            return self.query(2 * node + 1, mid + 1, end, ql, qr)
        
        left_prod, left_cnt = self.query(2 * node, start, mid, ql, qr)
        right_prod, right_cnt = self.query(2 * node + 1, mid + 1, end, ql, qr)
        
        res_prod = (left_prod * right_prod) % self.k
        res_cnt = [0] * self.k
        
        for r in range(self.k):
            res_cnt[r] += left_cnt[r]
            res_cnt[(left_prod * r) % self.k] += right_cnt[r]
            
        return res_prod, res_cnt

class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        ans = []
        
        for idx, val, start, x in queries:
            st.update(1, 0, n - 1, idx, val)
            _, cnt = st.query(1, 0, n - 1, start, n - 1)
            ans.append(cnt[x])
            
        return ans
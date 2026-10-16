class SegmentTree:
    def __init__(self, n):
        self.n = n
        # tree_sum1 维护区间 c 的和
        self.tree_sum1 = [0] * (4 * n)
        # tree_sum2 维护区间 c^2 的和
        self.tree_sum2 = [0] * (4 * n)
        # lazy 延迟标记
        self.lazy = [0] * (4 * n)

    def _push_down(self, node, l, r):
        if self.lazy[node] == 0:
            return
        
        add = self.lazy[node]
        mid = (l + r) // 2
        left_len = mid - l + 1
        right_len = r - mid
        
        # 更新左子节点
        self.tree_sum2[2 * node] += 2 * add * self.tree_sum1[2 * node] + add * add * left_len
        self.tree_sum1[2 * node] += add * left_len
        self.lazy[2 * node] += add
        
        # 更新右子节点
        self.tree_sum2[2 * node + 1] += 2 * add * self.tree_sum1[2 * node + 1] + add * add * right_len
        self.tree_sum1[2 * node + 1] += add * right_len
        self.lazy[2 * node + 1] += add
        
        self.lazy[node] = 0

    def update(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            # 根据 (c + 1)^2 = c^2 + 2c + 1 更新平方和
            self.tree_sum2[node] += 2 * self.tree_sum1[node] + (r - l + 1)
            self.tree_sum1[node] += (r - l + 1)
            self.lazy[node] += 1
            return
        
        self._push_down(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr)
            
        self.tree_sum1[node] = self.tree_sum1[2 * node] + self.tree_sum1[2 * node + 1]
        self.tree_sum2[node] = self.tree_sum2[2 * node] + self.tree_sum2[2 * node + 1]

class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = SegmentTree(n)
        
        last_seen = {}
        total_ans = 0
        
        for r, num in enumerate(nums):
            # 获取当前元素上一次出现的位置，如果没有出现过，左端点从 0 开始
            l = last_seen.get(num, -1) + 1
            
            # 对区间 [l, r] 的所有子数组计数加 1
            tree.update(1, 0, n - 1, l, r)
            
            # 记录当前元素的位置
            last_seen[num] = r
            
            # tree.tree_sum2[1] 存储的是当前状态下所有以 r 结尾的子数组的平方和
            total_ans = (total_ans + tree.tree_sum2[1]) % MOD
            
        return total_ans

# https://github.com/stevenhalim/cpbook-code/blob/master/ch2/ourown/fenwicktree_ds.py 
# Steven Halim Fenwick Tree implmentation
class FTree:
    def __init__(self, f):
        self.n = len(f)
        self.ft = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.ft[i] += f[i - 1]
            if i + self.lsone(i) <= self.n:
                self.ft[i + self.lsone(i)] += self.ft[i]

    def lsone(self, s):
        return s & (-s)

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)

        return s

    def update(self, i, v):
        while i <= self.n:
            self.ft[i] += v
            i += self.lsone(i)

    def select(self, k):
        p = 1
        while (p * 2) <= self.n: p *= 2

        i = 0
        while p > 0:
            if k > self.ft[i + p]:
                k -= self.ft[i + p]
                i += p
            p //= 2

        return i + 1

class RUPQ:
    def __init__(self, n):
        self.ftree = FTree([0] * n)

    def query(self, i):
        return self.ftree.query(1, i)

    def update(self, i, j, v):
        self.ftree.update(i, v)
        self.ftree.update(j + 1, -v)

class RURQ:
    def __init__(self, n):
        self.f = FTree([0] * n)
        self.r = RUPQ(n)

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)
        return self.r.query(j) * j - self.f.query(1, j)

    def update(self, i, j, v):
        self.r.update(i, j, v)
        self.f.update(i, v * (i - 1))
        self.f.update(j + 1, -1 * v * j)

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        tsum, temp_sum = 0, 0
        n = len(nums)
        r = RURQ(n)
        seen = {}

        for j, val in enumerate(nums):
            prev_index = seen.get(val,0)

            start = prev_index + 1 
            end = j + 1 # 1 based

            # cur distinct count 
            cur_sum = r.query(start, end)

            range_len = end - start + 1

            # (x + 1)^2 = x^2 + 2x + 1
            temp_sum = (temp_sum + cur_sum * 2 + range_len) % (10**9 + 7)

            tsum = (tsum + temp_sum) % (10**9 + 7)
            # apply range update (+1 distinct count) to the RURQ tree
            r.update(start, end, 1)

            # update last seen pos
            seen[val] = j + 1 

        return tsum % (10**9 + 7)
        
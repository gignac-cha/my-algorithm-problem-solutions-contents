class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        a = list(nums)
        while len(a) > 1:
            a = list(x + y for x, y in zip(a[:-1], a[1:]))
        return a.pop(0) % 10

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = len(nums) // 2
        l = 0
        r = n - 1
        while l <= r :
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1


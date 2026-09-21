class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        mlt_all = 1
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1
                continue
            mlt_all = mlt_all * num

        if count_zero > 1:
            k = len(nums)
            while(k>0):
                res.append(0)
                k -= 1
        elif count_zero == 1:
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(mlt_all)
        else:
            for num in nums:
                res.append(int(mlt_all/num))

        return res

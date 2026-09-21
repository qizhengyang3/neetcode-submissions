class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []

        for num, cnt in count.items():
            arr.append([cnt, num])
        
        arr.sort()

        res = []
        i = k
        while(i>0):
            res.append(arr.pop()[1])
            i = i -1
        
        return res

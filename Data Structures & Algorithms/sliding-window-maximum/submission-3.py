class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0, len(nums) - k + 1):
            max_e = nums[i]
            for j in range(i, i+k):
                max_e = max(max_e, nums[j])

            res.append(max_e)

        return res
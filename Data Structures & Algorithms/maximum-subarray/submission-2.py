class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        start = 0
        max_start = 0
        end = 0
        for i, num in enumerate(nums):
            if curr_sum <= 0:
                curr_sum = 0
                start = i

            curr_sum += num

            if curr_sum > max_sum:
                max_sum = curr_sum
                max_start = start
                end = i
        
        # print('Max Sub Array::', nums[max_start: end + 1])
        return max_sum

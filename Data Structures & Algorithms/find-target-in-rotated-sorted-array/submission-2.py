class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        pivot = l

        def binary_search(l, r):
            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
            
        result = binary_search(0, pivot -1)

        if result != -1:
            return result
        return binary_search(pivot, len(nums)-1)
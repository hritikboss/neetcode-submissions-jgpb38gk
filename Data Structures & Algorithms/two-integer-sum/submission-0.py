class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):          # pick first number
            for j in range(i + 1, len(nums)):  # pick second number
                if nums[i] + nums[j] == target:
                    return [i, j]
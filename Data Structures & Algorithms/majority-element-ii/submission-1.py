class Solution:
    def majorityElement(self, nums):
        count = {}
        ans = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        limit = len(nums) // 3

        for num in count:
            if count[num] > limit:
                ans.append(num)

        return ans
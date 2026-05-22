class Solution:
    def maxArea(self, heights: List[int]) -> int:
         # left pointer
        left = 0

        # right pointer
        right = len(heights) - 1

        # store maximum area
        max_water = 0

        # run until pointers meet
        while left < right:

            # calculate width
            width = right - left

            # smaller height decides water level
            height = min(heights[left], heights[right])

            # calculate current area
            area = width * height

            # update maximum area
            max_water = max(max_water, area)

            # move smaller height pointer
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water
from typing import List

def largest_container(heights: List[int]) -> int:

    if not heights or len(heights) < 2:
        return 0

    max_water = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        width = right - left

        current_height = min(heights[left], heights[right])

        current_area = width * current_height

        max_water = max(max_water, current_area)


        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

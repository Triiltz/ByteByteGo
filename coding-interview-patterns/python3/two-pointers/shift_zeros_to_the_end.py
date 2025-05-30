from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != insert_pos:
                nums[insert_pos] = nums[i]
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        single_numbers = []

        i = 0
        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                i += 2
                continue

            single_numbers.append(nums[i])
            i += 1

        if i < len(nums):
            single_numbers.append(nums[i])

        return single_numbers

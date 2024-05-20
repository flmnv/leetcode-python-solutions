class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def calculateXOR(num, nums: List[int]) -> list:
            if nums:
                return num + sum([
                    calculateXOR(num ^ nums[offset], nums[offset:])
                    for offset in range(1, len(nums))
                ])

            return num

        return sum([calculateXOR(nums[i], nums[i:]) for i in range(len(nums))])

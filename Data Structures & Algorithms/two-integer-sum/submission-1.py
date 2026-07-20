class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, v in enumerate(nums):
            val = target - v
            if val in temp:
                return [temp[val], i]
            else:
                temp[v] = i
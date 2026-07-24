class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(numbers)):
            val = target-numbers[i]
            if val in temp:
                return [temp[val], i + 1]
            else:
                temp[numbers[i]] = i + 1
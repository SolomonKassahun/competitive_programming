class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            output.append(summ)
        return output
        
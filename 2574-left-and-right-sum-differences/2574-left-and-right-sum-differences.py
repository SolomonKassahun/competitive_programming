class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightSum = 0
        leftSum = 0
        output = [0] * len(nums)
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)
        leftSum[0] = nums[0]
        rightSum[-1] = nums[-1]
        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i - 1] + nums[i] 
        for j in range((len(nums) - 2), -1, -1 ):
            rightSum[j] = rightSum[j + 1] + nums[j]
        for i in range(len(nums)):
            output[i] = abs(leftSum[i] - rightSum[i])
        return output
            
                
                
        
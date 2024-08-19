class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        leftProduct = [1] * n
        rightProduct = [1] * n
        for i in range(1, n):
            leftProduct[i] = nums[i - 1] * leftProduct[i - 1]
        for i in reversed(range(n - 1)):
            rightProduct[i] = nums[i + 1] * rightProduct[i + 1]

        for i in range(n):
            answer[i] = leftProduct[i] * rightProduct[i]

        return answer
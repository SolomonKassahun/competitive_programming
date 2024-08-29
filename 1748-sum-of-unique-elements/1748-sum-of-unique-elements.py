class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        totalSum = 0
        for ele, val in freq.items():
            if val == 1:
                totalSum += ele
        return totalSum
            
        
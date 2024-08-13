class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        max_length = 0
        for num, count in freq_map.items():
            if num + 1 in freq_map:
                max_length = max(max_length, count + freq_map[num + 1])
    
        return max_length
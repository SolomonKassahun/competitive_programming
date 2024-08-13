class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_than_pivot_items = []
        greater_than_pivot_items = []
        pivot_items = 0
        for item in nums:
            if item < pivot:
                smaller_than_pivot_items.append(item)
            elif item > pivot:
                greater_than_pivot_items.append(item)
            else:
                pivot_items += 1
        output =  smaller_than_pivot_items + [pivot] * pivot_items + greater_than_pivot_items
        return output
                
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            small, large = numbers[l], numbers[r]
            summ = small + large
            if summ == target:
                return [l+1, r+1]
            
            if summ < target:
                l += 1

            else:
                r -= 1
        
        return [l+1, r+1]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # identify starts of sequence = nbs with no nb 1 less than
        # find next number using set
        sett = set(nums)
        max_count = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in sett:
                count = 1
                nextt = nums[i] + 1
                while nextt in sett:
                    count += 1
                    nextt += 1
                max_count = max(max_count, count)

        return max_count                
        

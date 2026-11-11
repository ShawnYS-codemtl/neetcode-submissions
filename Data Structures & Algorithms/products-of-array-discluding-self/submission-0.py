class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # calculate the suffix from the end
        suffix = 1
        suff_arr = [1] * n
        for i in range(n-2,-1, -1):
            suffix = suffix * nums[i+1]
            suff_arr[i] = suffix

        # calculate the prefix from the start
        prefix = 1
        pref_arr = [1] * n
        for i in range(1, n):
            prefix = prefix * nums[i-1]
            pref_arr[i] = prefix
        
        # multiply
        output = []
        for i in range(n):
            output.append(pref_arr[i] * suff_arr[i])
        
        return output

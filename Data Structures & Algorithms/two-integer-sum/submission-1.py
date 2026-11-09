class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashh:
                if i < hashh[difference]:
                    return [i, hashh[difference]]
                else:
                    return [hashh[difference], i]
            else:
                hashh[nums[i]] = i
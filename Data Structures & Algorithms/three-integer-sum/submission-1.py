class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        seen = set()
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break

            if nums[i] in seen:
                i += 1
                continue
            
            seen.add(nums[i])

            l = i + 1
            r = len(nums)-1
            target = - (nums[i])
            triplets = set()
            while l < r:
                summ = nums[l] + nums[r]
                if summ == target:
                    if (nums[i], nums[l], nums[r]) not in triplets:
                        triplets.add((nums[i], nums[l], nums[r]))
                        result.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif summ < target:
                    l += 1
                else:
                    r -= 1
            
            i += 1

        return result

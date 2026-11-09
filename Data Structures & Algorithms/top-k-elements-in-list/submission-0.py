from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = defaultdict(list)
        for num, fr in freq.items():
            buckets[fr].append(num)
        
        res = []
        for key,buck in sorted(buckets.items(), reverse=True):
            for v in buck:
                res.append(v)
                if len(res) == k:
                    return res
        
        return res



        
        
            

 
   

            
            
        



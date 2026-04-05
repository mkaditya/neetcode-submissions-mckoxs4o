class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen_idx = {}
        for idx, num in enumerate(nums2):
            seen_idx[num] = idx
        
        result = []
        for num in nums1:
            if num not in seen_idx:
                return []
            
            result.append(seen_idx[num])
        return result
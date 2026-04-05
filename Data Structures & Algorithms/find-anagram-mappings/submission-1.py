class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # it seems we can do better with doing left shift of numbers by 7 digits and adding idx, sorting etc.,
        # basically bit magic to get the same result, we give up runtime complexity to save on space in such case.
        
        seen_idx = {}
        for idx, num in enumerate(nums2):
            seen_idx[num] = idx
        
        result = []
        for num in nums1:
            if num not in seen_idx:
                return []
            
            result.append(seen_idx[num])
        return result
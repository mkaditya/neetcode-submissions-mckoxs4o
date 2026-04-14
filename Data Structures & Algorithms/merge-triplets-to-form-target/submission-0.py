class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = False, False, False
        for t in triplets:
            x = x | (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y = y | (t[1] == target[1] and t[0] <= target[0] and t[2] <= target[2])
            z = z | (t[2] == target[2] and t[0] <= target[0] and t[1] <= target[1])
        
        if x and y and z:
            return True
        return False
        
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = 0
            rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')  # Impossible to make all values equal to x
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)
        
        # Try both candidates: tops[0] and bottoms[0]
        res = min(check(tops[0]), check(bottoms[0]))
        return res if res != float('inf') else -1

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r :
            cp = (l + r)// 2
            cw = 0 
            nd = 1
            for w in weights:
                if cw + w > cp:
                    nd += 1
                    cw = 0
                cw += w
            if nd <= days:
                r = cp -1
            else:
                l = cp + 1
        return l

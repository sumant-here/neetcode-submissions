class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l =  0
        mf = 0
        ans = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            mf = max(mf,count[s[r]])
            wd   = r - l + 1
            rp = wd  - mf
            if rp > k:
                count[s[l]] -= 1
                l +=1
            ans = max(ans,r -l+1)
        return ans
        
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        countT = Counter(t)
        window = {}
        have = 0 
        need = len(countT)
        left = 0 
        result = ""
        result_len = float("inf")
        for right in range(len(s)):
            char = s[right]
            # add current charactor to window 
            window[char] = window.get(char,0) + 1
            # did this charactor satisfy a requrement
            if char in countT and window[char] == countT[char]:
                have += 1
            # window is valid 
            while have == need:
                # check if current window is smalle r
                window_len = right - left + 1
                if window_len < result_len:
                    result = s[left:right +1]
                    result_len = window_len
                # remove left charactor
                left_char = s[left]
                window[left_char] -= 1
                #removing it made the window invalid
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                left += 1
        return result 
        
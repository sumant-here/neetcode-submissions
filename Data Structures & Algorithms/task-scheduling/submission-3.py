class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values()) # max freq kete jauchi 
        countMax = 0 #  kete janakr max freq ach
        for f in freq.values():
            if f == maxFreq:
                countMax += 1  #THIS REpresent how many hav max freq
        part =(maxFreq - 1) * (n + 1) + countMax
        return max(len(tasks),part)
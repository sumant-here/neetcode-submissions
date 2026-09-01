class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dl = defaultdict(int)
        for  inc,out in trust:
            dl[inc] -= 1 # outgi=oing trust 
            dl[out] += 1 # incoming trust
        for i in range(1, n + 1):
            if dl[i] ==  n - 1:
                return  i 
        return - 1
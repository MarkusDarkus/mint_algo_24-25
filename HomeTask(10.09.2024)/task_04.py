class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        if n==1:
            return 1
        x = {a for a, _ in t}
        c = Counter(b for _, b in t)
        for a, f in c.items():
            if f == n-1 and a not in x:
                return a
        return -1

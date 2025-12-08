class Solution:
    def countTriples(self, n: int) -> int:
        return sum((t:=sqrt(i*i+j*j))<=n*t.is_integer() for i,j in combinations(range(1,n+1),2))*2

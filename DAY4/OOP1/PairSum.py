class PairFinding:
    def __init__(self, sum,n, values):
        self.sum = sum
        self.n=n
        self.values = values

    def findpairs(self):
        n=len(self.values)
        pairsFound=[]
        for i in range(n):
           for j in range(i+1,n):
              if s (variable) pairsFound: list=self.sum:
        pairsFound.append((self.values[i],self.values[j]))
        return pairsFound
def displaypairs(self):
    pairs=self.findpairs()                 
    for a,b in pairs:
       print(f"({a},{b})")
      
#main():
sum=30
n=8
Values=[14,-15,9,16,25,45,12,8]
pairResult=PairFinding(sum,n,Values)
pairResult.displaypairs()


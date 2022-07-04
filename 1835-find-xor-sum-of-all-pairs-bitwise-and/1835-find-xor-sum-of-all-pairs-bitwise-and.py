class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        #O(N)
        xor1,xor2=0,0
        
        for i in arr1:
            xor1^=i
            
        for i in arr2:
            xor2^=i
        
        return xor1&xor2
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        #It simplifies to checking if the XOR of the entire range from i to k is zero.
        #I will use prefix XOR array 
        n = len(arr)
        prefixXOR = [0] * (n+1) #Initialize 
        
        for i in range(n):
            prefixXOR[i+1] = prefixXOR[i] ^ arr[i] #Compute
            
        #Now, we iterate through all possible pairs (i,k)
        count = 0
        for i in range(n):
            for k in range(i+1, n):
                if prefixXOR[i] == prefixXOR[k+1]:
                    count += (k-i)
                    
        return count
                    
            
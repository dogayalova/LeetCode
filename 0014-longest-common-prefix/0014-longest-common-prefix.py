class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] #Initialize prefix
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1] #Remove last chcrtr until it becomes a common prefix
                
        return prefix
            

            
        
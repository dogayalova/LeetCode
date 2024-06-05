class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        common_char = list(words[0])
        
        for word in words[1:]:
            new_common_char = [] 
            for letter in word:
                if letter in common_char:
                    new_common_char.append(letter)
                    common_char.remove(letter)
                    
            common_char = new_common_char
            
        return common_char

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Sort dictionary to ensure shorter roots are considered first
        dictionary.sort(key=len)
        
        # Split the sentence into words
        words = sentence.split()
        
        # Iterate over each word and replace it if a root is found
        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break  # Once we find the root, we can stop checking further
        
        # Join the words back into a sentence
        return ' '.join(words)
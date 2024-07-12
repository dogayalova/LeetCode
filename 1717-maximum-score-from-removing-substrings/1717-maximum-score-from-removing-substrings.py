class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        result = 0
        
        def remove_and_score(s, first, second, first_points, second_points):
            stack = []
            score = 0
            
            for char in s:
                if stack and stack[-1] + char == first:
                    stack.pop()
                    score += first_points
                else:
                    stack.append(char)
            
            new_string = []
            for char in stack:
                if new_string and new_string[-1] + char == second:
                    new_string.pop()
                    score += second_points
                else:
                    new_string.append(char)
            
            return score
        
        if x > y:
            result = remove_and_score(s, "ab", "ba", x, y)
        else:
            result = remove_and_score(s, "ba", "ab", y, x)
        
        return result
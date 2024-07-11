class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current_string = []
    
        for char in s:
            if char == '(':
                # Push the current string to stack and start a new one
                stack.append(current_string)
                current_string = []
            elif char == ')':
                # Reverse the current string and append to the previous one in the stack
                current_string.reverse()
                if stack:
                    current_string = stack.pop() + current_string
            else:
                # Add the current character to the current string
                current_string.append(char)

        # Join the characters to form the final result string
        return ''.join(current_string)

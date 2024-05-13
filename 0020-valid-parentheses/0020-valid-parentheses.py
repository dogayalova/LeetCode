class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {")": "(", "}": "{", "]" : "["}
        for a in s:
            if a in matches.values():
                stack.append(a)
            elif a in matches.keys():
                if not stack or matches[a] != stack.pop():
                    return False
  
        if stack == []:
            return True
      

        
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        
        for i in logs:
            if i == "../":
                if counter <= 0:
                    continue
                else:
                    counter -= 1
            elif i == "./":
                continue
            else:
                counter += 1

        return counter
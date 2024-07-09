from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = []
        current_time = 0
        
        for customer in customers:
            arrival = customer[0]
            duration = customer[1]
            
            if current_time < arrival:
                current_time = arrival
                
            current_time += duration
            each = current_time - arrival
            time.append(each)
        
        average = sum(time) / len(time)
        return average
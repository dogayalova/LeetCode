class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Count the number of connections for each city
        connection_count = [0] * n
        for road in roads:
            connection_count[road[0]] += 1
            connection_count[road[1]] += 1
        
        # Step 2: Create a dictionary of cities and their connection counts
        max_road_dict = {i: connection_count[i] for i in range(n)}
        
        # Step 3: Sort cities by the number of connections in descending order
        sorted_by_keys_desc = dict(sorted(max_road_dict.items(), key=lambda item: item[1], reverse=True))
        
        # Step 4: Assign values to cities based on the sorted order
        assign_dict = {}
        value = n
        for city in sorted_by_keys_desc.keys():
            assign_dict[city] = value
            value -= 1
        
        # Step 5: Calculate the total importance of all roads
        result = 0
        for road in roads:
            node1, node2 = road
            result += assign_dict[node1] + assign_dict[node2]
                
        return result
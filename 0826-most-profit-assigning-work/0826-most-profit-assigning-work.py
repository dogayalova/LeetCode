class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit into a list of tuples and sort them
        jobs = sorted(zip(difficulty, profit))
        # Sort the worker array
        worker.sort()

        max_profit = 0
        job_index = 0
        best_profit = 0

        # Iterate through each worker
        for ability in worker:
            # Update best_profit to the maximum profit the worker can achieve based on their ability
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1
            # Add the best profit the worker can achieve to the total profit
            max_profit += best_profit

        return max_profit

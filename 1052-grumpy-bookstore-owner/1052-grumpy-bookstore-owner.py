class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #sliding windows of size "minutes"
        def max_sum_subarray(arr, k):
            n = len(arr)
            if n < k:
                return -1, []  # Not enough elements

            max_sum = sum(arr[:k])
            window_sum = max_sum
            max_start_index = 0

            for i in range(1, n - k + 1):
                window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
                if window_sum > max_sum:
                    max_sum = window_sum
                    max_start_index = i

            # The indices of the optimal window
            optimal_indices = list(range(max_start_index, max_start_index + k))
            return max_sum, optimal_indices
        
     # Calculate the number of satisfied customers without using the technique
        satisfied_customers = sum(c for c, g in zip(customers, grumpy) if g == 0)
        
        # Calculate the potential maximum increase in satisfied customers using the technique
        # Here, we calculate the additional customers we can satisfy during the grumpy minutes
        extra_customers = [customers[i] if grumpy[i] == 1 else 0 for i in range(len(customers))]
        max_extra_satisfied, opt_indices = max_sum_subarray(extra_customers, minutes)

        # The total maximum satisfied customers
        total_satisfied = satisfied_customers + max_extra_satisfied

        return total_satisfied
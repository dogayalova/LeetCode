class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        student = sorted(students)
        result = []
        for i in range(len(seats)):
            result.append(abs(seats[i]-student[i]))
        return sum(result)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        result += numBottles
        while numBottles >= numExchange:
            result += numBottles // numExchange
            numBottles = numBottles // numExchange + (numBottles % numExchange)
        return result
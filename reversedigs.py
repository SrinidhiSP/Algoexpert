class Solution:
    def reversedigs(x:int) -> int:
        result, remaining_x = 0, abs(x)
        while remaining_x:
            result = result * 10 + remaining_x / 10
            remaining_x //= 10
        return -result if x < 0 else result
        

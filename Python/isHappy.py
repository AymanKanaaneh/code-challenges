class Solution:
    def isHappy(self, n: int) -> bool:
        sumDSquare = 0
        sumDSquareDic = set()

        while n not in sumDSquareDic:
            sumDSquareDic.add(n)
            while n != 0:
                sumDSquare += (n % 10)**2
                n = math.floor(n / 10)

            if sumDSquare == 1:
                return True

            n = sumDSquare
            sumDSquare = 0
        
        return False
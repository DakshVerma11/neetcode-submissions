class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        upperBound, lowerBound = 0, len(matrix) - 1
        leftBound, rightBound = 0, len(matrix[0]) - 1
        res = []

        while upperBound <= lowerBound and leftBound <= rightBound:
            for i in range(leftBound, rightBound + 1):
                res.append(matrix[upperBound][i])
            upperBound += 1

            for j in range(upperBound, lowerBound + 1):
                res.append(matrix[j][rightBound])
            rightBound -= 1

            if upperBound <= lowerBound:
                for i in range(rightBound, leftBound - 1, -1):
                    res.append(matrix[lowerBound][i])
                lowerBound -= 1

            if leftBound <= rightBound:
                for j in range(lowerBound, upperBound - 1, -1):
                    res.append(matrix[j][leftBound])
                leftBound += 1

        return res
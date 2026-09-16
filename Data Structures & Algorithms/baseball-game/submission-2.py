class Solution:
    def calPoints(self, operations: List[str]) -> int:
        totalSum = 0
        currentScores = []
        for operation in operations:
            if operation == "+":
                currentScores.append(
                    currentScores[-1] + currentScores[-2]
                )
                totalSum += currentScores[-1]
            elif operation == "D":
                currentScores.append(
                    currentScores[-1] * 2
                )
                totalSum += currentScores[-1]
            elif operation == "C":
                totalSum -= currentScores[-1]
                currentScores.pop()
            else:
                currentScores.append(int(operation))
                totalSum += currentScores[-1]
        return totalSum

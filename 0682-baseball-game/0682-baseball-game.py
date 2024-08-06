class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []
        for op in operations:
            if op == '+':
                if len(output) >= 2:
                    output.append(output[-1] + output[-2])
            elif op == 'D':
                if output:
                    output.append(output[-1] * 2)
            elif op == 'C':
                if output:
                    output.pop()
            else:
                output.append(int(op))
        return sum(output)

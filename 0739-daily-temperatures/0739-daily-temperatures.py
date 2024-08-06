class Solution:
    def dailyTemperatures(self, temperatures):
        s = len(temperatures)
        a = []
        answer = [0] * s

        for i in range(s):
            while a and temperatures[a[-1]] < temperatures[i]:
                prev_index = a.pop()
                answer[prev_index] = i - prev_index
            a.append(i)

        return answer
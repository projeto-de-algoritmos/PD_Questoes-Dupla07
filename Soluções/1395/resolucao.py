class Solution:
    def numTeams(self, rating):
        n = len(rating)
        cnt = 0
        for j in range(n):
            less_left, less_right, greater_left, greater_right = 0, 0, 0, 0
            for i in range(j):
                if rating[i] < rating[j]:
                    less_left += 1
                else:
                    greater_left += 1
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    less_right += 1
                else:
                    greater_right += 1
            cnt += less_left * less_right + greater_left * greater_right
        return cnt

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = max(1 + candies[i], candies[i+1])
                
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                candies[i] = max(1 + candies[i+1], candies[i])
        return sum(candies)
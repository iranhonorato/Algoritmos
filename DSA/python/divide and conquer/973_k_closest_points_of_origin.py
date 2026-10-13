class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        ans = list()
        map = list()

        for i in range(len(points)):
            point = points[i]
            d = ((point[0])**2 + (point[1])**2)**0.5
            map.append((d, i))

        map.sort()

        for j in range(k):
            ans.append(points[map[j][1]])

        return ans
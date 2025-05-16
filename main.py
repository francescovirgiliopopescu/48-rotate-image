from typing import List

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    if len(matrix) == 0:
      return
    h = len(matrix)
    w = len(matrix[0])
    for i in range(0, h): # mirror
      for j in range(0, w // 2):
        matrix[i][j], matrix[i][w - j - 1] = matrix[i][w - j - 1], matrix[i][j]

    for i in range(0, h): # transpos
      for j in range(0, w - 1 - i):
        matrix[i][j], matrix[w - 1 - j][h - 1 - i] = matrix[w - 1 - j][h - 1 - i], matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

sol = Solution()
sol.rotate(matrix)
print(matrix)
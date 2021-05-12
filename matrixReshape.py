def matrixReshape(mat, r, c):
  totalMatRow = len(mat)
  totalMatCol = len(mat[0])
  totalElements = totalMatRow * totalMatCol

  if totalElements != r*c:
    return mat
  
  array = []
  colCount = 0
  for i in range(totalMatRow):
    for j in range(totalMatCol):
      if colCount == 0:
        array.append([])

      array[len(array)-1].append(mat[i][j])

      colCount += 1
      if colCount == c:
        colCount = 0
      
  
  return array

matrixReshape([[1,2,3,4]], 2, 2)
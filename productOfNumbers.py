class ProductOfNumbers:
  def __init__(self):
    self.stack = []
      

  def add(self, num: int) -> None:
    if num == 0:
      self.stack = []
    elif len(self.stack) == 0:
      self.stack.append(num)
    else:    
      ans = num*(self.stack[len(self.stack)-1])
      self.stack.append(ans)
    

  def getProduct(self, k: int) -> int:
    if k > len(self.stack):
      return 0
    if len(self.stack) == k:
      return self.stack[len(self.stack)-1]

    return self.stack[len(self.stack)-k-1] // self.stack[len(self.stack)-k-1]

productOfNumbers = ProductOfNumbers();
productOfNumbers.add(3);        # [3]
productOfNumbers.add(0);        # [3,0]
productOfNumbers.add(2);        # [3,0,2]
productOfNumbers.add(5);        # [3,0,2,5]
productOfNumbers.add(4);        # [3,0,2,5,4]
productOfNumbers.getProduct(2); # return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        # [3,0,2,5,4,8]
productOfNumbers.getProduct(2); # return 32. The product of the last 2 numbers is 4 * 8 = 32 

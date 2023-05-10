def isPalindrome(x: int) -> bool:        
  if x < 0: return False
  strX = str(x)
  for i in range(len(strX)):
      print(strX[i], strX[-(i+1)])
      if (len(strX)%2==1 and i == (len(strX)-1)/2) or (len(strX)%2==0 and i > len(strX)/2):
          return True
      if strX[i] != strX[-(i+1)]:
          return False
  return True
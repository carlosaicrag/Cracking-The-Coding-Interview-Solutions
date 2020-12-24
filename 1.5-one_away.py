def one_away(str1,str2):
  def edit():
    foundDifference = False
    i = 0

    while i < len(str1):
      if str1[i] != str2[i]:
        if foundDifference:
          return False
        foundDifference = True
      i += 1

    return True

  def insert_remove(str1,str2):
    foundDifference = False
    i = 0 
    j = 0 

    while i < len(str1) and j < len(str2):
      if str1[i] != str2[j]:
        if foundDifference:
          return False
        foundDifference = True 
        j += 1
      else:
        i += 1
        j += 1

    return True
    
  if len(str1) == len(str2):
    return edit()
  elif len(str1) + 1 == len(str2):
    return insert_remove(str1,str2)
  elif len(str1) - 1 == len(str2):
    return insert_remove(str2,str1)
  else:
    return False



print(one_away("pale","ple"))
print(one_away("pales","pale"))
print(one_away("pale","bale"))
print(one_away("pale","bake"))
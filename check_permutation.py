def check_permutation(str1,str2):
  if len(str1) != len(str2):
    return False

  d1 = {}
  d2 = {}

  for letter in str1:
    if letter not in d1:
      d1[letter] = 1
    else:
      d1[letter] += 1
  
  for letter in str2:
    if letter not in d2:
      d2[letter] = 1
    else:
      d2[letter] += 1

  for key in d1:
    if key not in d2:
      return False
    if d2[key] != d1[key]:
      return False

  return True

print(check_permutation("ctb","bat"))
print(check_permutation("atb","bat"))

    
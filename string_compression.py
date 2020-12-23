def compression(str1):
  if len(str1) == 0:
    return ""

  result = ""
  count = 1
  i = 1

  while i < len(str1):
    if str1[i] != str1[i-1]:
      result += str1[i-1] + str(count)
      count = 1
    else:
      count += 1 
    i += 1

  result += str1[-1] + str(count)
  return result

print(compression("aabccccaaa"))
print(compression(""))
print(compression("a"))
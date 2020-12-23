def english_int(integer):
  numbers = {
    "1": "one",
    '2': "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
  }
  oneth = ["", "thousand", "million", "billion", "trillion"]
  tenth = {
    "2":"twenty", 
    "3":"thirty", 
    "4":"fourty", 
    "5":"fifty", 
    "6":"sixty", 
    "7":"seventy",
    "8":"eighty",
    "9":"ninety"
    }
  special = {
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifthteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
  }

  int_str = list(str(integer))
  int_str.reverse()
  result = []
  current_oneth = 0

  for idx,letter in enumerate(int_str):
    if idx%3 == 0:
      print(letter)
      result.append(numbers[letter] + " " + oneth[current_oneth])
      current_oneth += 1
    elif idx%3 == 1:
      if letter == "1":
        result[-1] = ""
        special_number = letter + int_str[idx-1]
        result.append(special[special_number])
      else:
        result.append(tenth[letter])
    elif idx%3 == 2:
      result.append(numbers[letter]+ " " + "hundred")

  result.reverse()

  return " ".join(result)




print(english_int(1234))
print(english_int(1212))
print(english_int(121256))
print(english_int(1234567891))
print(english_int(2147483648))
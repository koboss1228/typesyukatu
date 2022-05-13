def fizzbuzz():
  for i in range(100):
    j = i+1
    if j % 15 == 0: # jが15の倍数の場合
      print("FizzBuzz")
    elif j % 3 == 0: # jが3の倍数の場合
      print("Fizz")
    elif j % 5 == 0: # jが5の倍数の場合
      print("Buzz")
    else: # その他の場合
      print(j)
      
fizzbuzz()

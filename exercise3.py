"""
arrayをソートし、2つのarrayを出力する関数。
"""
def sort_algo(array):
  length = len(array)
  if length == 0:
    return
  elif length == 1:
    return array
  elif length == 2:
    if array[0] < array[1]:
      return array
    elif array[1] < array[0]:
      a = array[0]
      b = array[1]
      array[0] = b
      array[1] = a
      return array
  standard_value = array[0]
  for i in range(length): # arrayの左からstandard_value以上の数字を探す。
    if array[i] >= standard_value: # 
        a = array[i]
        for j in range(length): # arrayの右からstandard_value未満の数字を探す。
          k = (length - 1) - j
          if i == k: # 左右それぞれから探して、同じ要素を指した場合。
            if i == 0:
              continue
            else:
              array_less_val = array[0:i] # standard_value未満の数字を含んだarray。
              array_eq_greater_val = array[i:length] # standard_value以上の数字を含んだarray。
              return array_less_val, array_eq_greater_val
          elif array[k] < standard_value:
            b = array[k]
            array[i] = b # 左から選んだstandard_value以上の数字を右から選んだstandard_value未満の数字に置き換える。
            array[k] = a # 左から選んだstandard_value未満の数字を右から選んだstandard_value以上の数字に置き換える。
            break
            
"""
sort_algoを使って、繰り返し呼び出しを行うことで、元のarrayを綺麗に並べる関数。
"""
def sort_algo_rep(array):
  box = [] # 数字を昇順にならべるarray。
  res = sort_algo(array)
  for i in range(len(res)):
    if type(res[i]) == int: # arrayの要素がintの場合。
      box.extend([res[i]]) # 数字をboxに入れる。
    else: # arrayの要素がarrayの場合。
      box.extend(sort_algo_rep(res[i])) # もう一度sort_algoを使って、さらに整理し、それぞれの要素がintになったものをboxに入れる。
  return box

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
  for i in range(length):
    if array[i] >= standard_value:
        a = array[i]
        for j in range(length):
          k = (length - 1) - j
          if i == k:
            if i == 0:
              continue
            else:
              array_less_val = array[0:i]
              array_eq_greater_val = array[i:length]
              return array_less_val, array_eq_greater_val
          elif array[k] < standard_value:
            b = array[k]
            array[i] = b
            array[k] = a
            break
            
            
def sort_algo_rep(array):
  box = []
  res = sort_algo(array)
  for i in range(len(res)):
    if type(res[i]) == int:
      box.extend([res[i]])
    else:
      box.extend(sort_algo_rep(res[i]))
  return box

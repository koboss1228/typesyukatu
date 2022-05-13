def binary_search(array, target):
  min_repository = [] # 新しいarrayを再定義する前に、minの値を保存しておくためのarray
  while len(array) >= 2: 
    min = 0 
    max = len(array) - 1 
    middle = max // 2 
    if array[middle] == target:
      min_repository.append(middle) # middleをindexの情報として保存する。
      target_index = sum(min_repository) # 今までに保存していたindexの情報について和をとる。
      return target_index
    elif target < array[middle]:
      array = array[min:(middle+1)] # middleよりも小さいindexについて新しいarrayを再定義する。
    elif array[middle] < target:
      min = middle + 1
      array = array[min:(max+1)] # middleよりも大きいinidexについて新しいarrayを再定義する。
      min_repository.append(min) # minの値をindexの情報として保存する。
  else:
    if len(array) == 0:
      return -1
    elif array[0] == target:
      target_index = sum(min_repository)
      return target_index
    else:
      return -1

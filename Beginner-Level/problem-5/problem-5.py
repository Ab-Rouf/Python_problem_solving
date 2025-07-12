def flatten_list(nested_list):
  f_list=[]
  for elements in nested_list:
    if isinstance(elements,list):
      f_list.extend(flatten_list(elements))
    else:
      f_list.append(elements)
  return f_list
list1=[1, [2, 3], [4, [5]]]
print(flatten_list(list1))

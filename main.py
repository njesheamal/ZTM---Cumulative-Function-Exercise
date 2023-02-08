def highest_even(li):
  even_nums = []
  for items in li:
    if (items % 2 == 0):
      even_nums.append(items)
  top_even_num = sorted(even_nums)
  return top_even_num[-1]

print(highest_even([10,2,3,4,7,11,24]))
def square_digits(num):
  num = list(str(num))
  nums = []
  for i in num:
    nums.append(str(int(i)**2))
  return int(''.join(nums))
idx = 0
x = 65
nums = [1,2,7,10,5,18,35,65,28]
for val in nums:
    if (val == x):
        print(f"{x} found at index = {idx}")
        break
    idx += 1
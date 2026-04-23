# Methods in List
# l.append(val) - Add one element at the end
# l.insert(idx,val) - Insert element at idx
# l.sort() - arranges in increasing order
# l.reverse() - reverses order

nums = [1,5,2,4]
# append
nums.append(7)
print(nums)
# insert
nums.insert(5,3)
print(nums)
# sort - sorts in ascending order
nums.sort()
print(nums)
# reverse = True - sorts in descending order
nums.sort(reverse=True)
print(nums)
# reverse - just flip the order
nums.reverse()
print(nums)
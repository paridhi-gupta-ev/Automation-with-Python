mat=[[1,2,3],[4,5,6],[7,8,9]]
print(mat)
names = ["John","Jane","George"]
print(names)
print(names[0])
print(len(names))
print(len(mat))
print(names[0:])
print(names[:])
for row in mat:
    for item in row:
        print(item)

nums = [6,9,5,4,0,8,7,3]
print(nums)
nums.append(20)
print(nums)
nums.insert(1,7)
print(nums)
nums.remove(8)
print(nums)
# nums.clear()
# print(nums)
print(nums.index(9))
print(5 in nums)
print(nums.count(0))
nums.sort()
print(nums)
num2 = nums.copy()
print(num2)
uniques=[]
for item in nums:
    if item not in uniques:
        uniques.append(item)

print(uniques)


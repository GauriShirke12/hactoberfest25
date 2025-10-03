nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_nums = []
for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)

print("After removing duplicates:", unique_nums)

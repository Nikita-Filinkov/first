nums = [0, 0, 1, 1, 2, 1, 2, 3, 4, 3]
nums.sort()
len_nums = 0
for i in nums:
    count_nums = nums.count(i)
    for d in range(count_nums):
        nums.remove(i)
        nums.append(" ")
        print(f"{count_nums}")
        if count_nums == 1:
            len_nums += 1
            break
    if i == " ":
        break
    # while count_nums > 1:
    #     nums.remove(i)
    #     nums.append("_")
    #     if count_nums == 1:
    #         len_nums += 1
    #         break
print(f"{nums}")

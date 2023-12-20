nums = [2, 1]
nums.sort()
len_nums = 0
if len(nums) == 1:
    len_nums = 1
else:
    while True:
        for i in nums:
            count_nums = nums.count(i)
            if count_nums > 1:
                nums.remove(i)
                nums.append(" ")
            elif count_nums == 1:
                break
        if " " in nums:
            break
    for num in nums:
        if num == " ":
            break
        len_nums += 1
print(f"Длина повторяющихся символов: {len_nums} ")
print(f"{nums}")

# ========================
# Q9: Elements appearing more than once
# ========================
nums = [1, 2, 3, 2, 4, 1, 5]
s=set()
for i in nums:
    if i not in s:
        s.add(i)
    else:
        print(i)
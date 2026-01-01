orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

nums = []
sort_oreds = []

for order in orders:
    nums.append(order[0])

nums.sort()

for num in nums:
    for order in orders:
        if num == order[0]:
            sort_oreds.append(order)
            
print(sort_oreds)
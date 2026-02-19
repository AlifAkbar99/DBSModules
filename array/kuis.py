var_array = [i for i in range(101)]
total = 0
for value in var_array:
    total += value   
panjang_array = len(var_array)
if panjang_array > 0:
    result = total/panjang_array
else:
    result = 0
print(result)
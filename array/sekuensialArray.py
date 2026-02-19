var_arr = [1,2,3,4,5]

for i in range(len(var_arr)):
    current_element = var_arr[i] # metode indexing
    next_index = i + 1 # suksesor index
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f'current element: {current_element}, next element: {next_element} ')
    

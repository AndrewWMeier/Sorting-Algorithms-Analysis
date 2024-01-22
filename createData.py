import random
#this file holds functions to help in the anaylsis of algorithms


#generate random arrays of size arr_size, number num_arrays, and integer range integer_range
def generate_arrays(arr_size, num_arrays, integer_range):
    arrays = []
    for i in range(num_arrays):
        arr = []
        for j in range(arr_size):
            arr.append(random.randint(0, integer_range))
        arrays.append(arr)
    return arrays





import random
import numpy

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

#takes array of excecution times and returns the average, median, standard deviation, max, min
def get_execution_stats(execution_times):
    average = numpy.average(execution_times)
    median = numpy.median(execution_times)
    max_time = max(execution_times)
    min_time = min(execution_times)
    stddev = numpy.std(execution_times)
    return average, median, max_time, min_time, stddev






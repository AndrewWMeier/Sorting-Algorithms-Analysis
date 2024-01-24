from createData import generate_arrays
from createData import get_execution_stats
import timeit
import matplotlib.pyplot as plt
#this file does the main analysis of merge sort

#merge sort algorithm
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr

#takes a 2d array of arrays and returns an array of execution times for the sorting time of each array
def algorithm_analysis(arrays):
    execution_times = []
    for arr in arrays:
        start_time = timeit.default_timer()
        mergeSort(arr)
        execution_times.append(timeit.default_timer() - start_time)
    return execution_times

#graphing the median execution time vs array size for merge sort
def plot_execution_times(array_sizes, num_arrays, integer_range,plot_type):
    median_execution_times = []
    average_execution_times = []
    max_execution_times = []
    min_execution_times = []
    stddev_execution_times = []

    for size in array_sizes:
        #generate arrays
        test_data = generate_arrays(size, num_arrays, integer_range)

        #get execution time of mergesort for each array
        execution_times = algorithm_analysis(test_data)

        #get median execution time for each array size
        median_execution_time = get_execution_stats(execution_times)[1]
        median_execution_times.append(median_execution_time)

        #get average execution time for each array size
        average_execution_time = get_execution_stats(execution_times)[0]
        average_execution_times.append(average_execution_time)

        #get max/min execution time for each array size
        max_execution_times.append(get_execution_stats(execution_times)[2])
        min_execution_times.append(get_execution_stats(execution_times)[3])

        #get standard deviation of execution times for each array size
        stddev_execution_times.append(get_execution_stats(execution_times)[4])
 
    # plot graph of execution times vs array size
    plt.figure(figsize=(10, 6))

    if plot_type == "Median":
        plt.errorbar(array_sizes, median_execution_times, yerr=stddev_execution_times, fmt='o-', label='Median')
        plt.title("Merge Sort Median Execution Times")
        plt.xlabel("Array Size")
        plt.ylabel("Execution Time (s)")
        plt.show()

    elif plot_type == "Average":
        plt.errorbar(array_sizes, average_execution_times,yerr=stddev_execution_times, fmt='o-', label='Average')
        plt.title("Merge Sort Average Execution Times")
        plt.xlabel("Array Size")
        plt.ylabel("Execution Time (s)")
        plt.show()

# [10000, 40000, 70000, 100000, 130000, 160000, 190000, 220000]

# Call the function to plot the graph
    #in this case we are plotting median and average execution times for 10 arrays of sizes 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000. 
    #these arrays are filled with random integers from 0 to 1000
# plot_execution_times([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000], 10, 1000)
    







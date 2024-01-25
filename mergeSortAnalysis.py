from createData import generate_arrays
from createData import get_execution_stats
from createData import get_avg_comparisons
import timeit
import matplotlib.pyplot as plt
#this file does the main analysis of merge sort

#merge sort algorithm that also counts its comparisons
def mergeSort(arr, comparisons=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        comparisons = mergeSort(left, comparisons)
        comparisons = mergeSort(right, comparisons)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            comparisons += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return comparisons


#takes a 2d array of arrays and returns an array of execution times for the sorting time of each array, and an array of the number of comparisons for each array
def algorithm_analysis(arrays):
    execution_times = []
    comparisons_list = []
    for arr in arrays:
        start_time = timeit.default_timer()
        comparisons = mergeSort(arr.copy())
        execution_times.append(timeit.default_timer() - start_time)
        comparisons_list.append(comparisons)
    return execution_times, comparisons_list

#graphing the median execution time vs array size for merge sort
def plot_execution_times(array_sizes, num_arrays, integer_range,plot_type):
    median_execution_times = []
    average_execution_times = []
    max_execution_times = []
    min_execution_times = []
    stddev_execution_times = []
    avg_comparisons = []

    for size in array_sizes:
        #generate arrays
        test_data = generate_arrays(size, num_arrays, integer_range)

        #get execution time of mergesort for each array and number of comparisons in a seperate array
        execution_times, comparisons_list = algorithm_analysis(test_data)
      
        #get average number of comparisons for each array size
        avg_comparisons.append(get_avg_comparisons(comparisons_list))

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
    #median and avg have the std deviation as error bars 
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

    elif plot_type == "Comparisons":
        # plot graph of average number of comparisons vs array size
        plt.plot(array_sizes, avg_comparisons, 'o-', label='Average') 
        plt.title("Merge Sort Average Number of Comparisons")
        plt.xlabel("Array Size")
        plt.ylabel("Number of Comparisons")
        plt.show()

    elif plot_type == "Max/Min":
        #plot graph of max/min execution times vs array size
        plt.plot(array_sizes, max_execution_times, 'o-', label='Max')
        plt.plot(array_sizes, min_execution_times, 'o-', label='Min')
        plt.title("Merge Sort Max/Min Execution Times")
        plt.xlabel("Array Size")
        plt.ylabel("Execution Time (s)")
        plt.legend()
        plt.show()







from createData import generate_arrays
import timeit

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

#test
arrays = generate_arrays(10, 10, 1000)
print(algorithm_analysis(arrays))





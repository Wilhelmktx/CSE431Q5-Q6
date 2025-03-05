import timeit
import random

import sys
sys.setrecursionlimit(1500)
import csv

MIN_MERGE = 32

#Obtained from here: https://www.geeksforgeeks.org/tim-sort-in-python/
def insertionTim(arr, left=0, right=None):
    # Base case: if the array is already sorted, do nothing
    if right is None:
        right = len(arr) - 1

    # Iterate through the array, starting from the second element
    for i in range(left + 1, right + 1):
        # Select the current element
        key_item = arr[i]

        # Compare the current element with the previous one
        j = i - 1

        # While the previous element is greater than the current one,
        # shift the previous element to the next position
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1

        # Once the loop ends, the previous element is less than or equal to
        # the current element, so place the current element after it
        arr[j + 1] = key_item

    return arr

def mergeTim(left, right):
    # If the left subarray is empty, return the right subarray
    if not left:
        return right

    # If the right subarray is empty, return the left subarray
    if not right:
        return left

    # Compare the first elements of the two subarrays
    if left[0] < right[0]:
        # If the first element of the left subarray is smaller,
        # recursively merge the left subarray with the right one
        return [left[0]] + mergeTim(left[1:], right)
    else:
        # If the first element of the right subarray is smaller,
        # recursively merge the right subarray with the left one
        return [right[0]] + mergeTim(left, right[1:])

def tim_sort(arr):
    # Initialize the minimum run size
    min_run = 32

    # Find the length of the array
    n = len(arr)

    # Traverse the array and do insertion sort on each segment of size min_run
    for i in range(0, n, min_run):
        insertionTim(arr, i, min(i + min_run - 1, (n - 1)))

    # Start merging from size 32 (or min_run)
    size = min_run
    while size < n:
        # Divide the array into merge_size
        for start in range(0, n, size * 2):
            # Find the midpoint and endpoint of the left and right subarrays
            midpoint = start + size
            end = min((start + size * 2 - 1), (n - 1))

            # Merge the two subarrays
            merged_array = mergeTim(arr[start:midpoint], arr[midpoint:end + 1])

            # Assign the merged array to the original array
            arr[start:start + len(merged_array)] = merged_array

        # Increase the merge size for the next iteration
        size *= 2

    return arr


#From https://www.geeksforgeeks.org/python-program-for-insertion-sort/#
def insertionSort(arr):

    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position

#From https://www.geeksforgeeks.org/python-program-for-merge-sort/
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted

#From https://www.geeksforgeeks.org/python-program-for-merge-sort/
def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def comparison(lis):

    lis1=lis.copy()
    lis2=lis.copy()
    lis3=lis.copy()

    start = timeit.default_timer()
    insertionSort(lis1)
    end = timeit.default_timer()

    start2 = timeit.default_timer()
    mergeSort(lis2, 0, len(lis2)-1)
    end2 = timeit.default_timer()

    start3 = timeit.default_timer()
    tim_sort(lis3)
    end3 = timeit.default_timer()

    return [end - start, end2 - start2, end3 - start3]


lis = []
lis.append(["Insertion Sort", "Merge Sort", "Tim Sort"])
for i in range(50):
    og = random.sample(range(0, 1000), 1000)

    test0 = og[:2]
    test0_3 = og[:3]
    test0_4 = og[:4]
    test0_5 = og[:5]
    test0_6 = og[:6]
    test0_7 = og[:7]
    test0_8 = og[:8]
    test0_9 = og[:9]
    test1 = og[:10]
    test2 = og[:20]
    test3 = og[:30]
    test4 = og[:40]
    test5 = og[:50]

    test6 = og[:100]
    test7 = og[:500]
    test8 = og[:1000]

    lis.append(comparison(test0))
    lis.append(comparison(test0_3))
    lis.append(comparison(test0_4))
    lis.append(comparison(test0_5))
    lis.append(comparison(test0_6))
    lis.append(comparison(test0_7))
    lis.append(comparison(test0_8))
    lis.append(comparison(test0_9))

    lis.append(comparison(test1))
    lis.append(comparison(test2))
    lis.append(comparison(test3))
    lis.append(comparison(test4))
    lis.append(comparison(test5))
    lis.append(comparison(test6))
    lis.append(comparison(test7))
    lis.append(comparison(test8))


with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lis)





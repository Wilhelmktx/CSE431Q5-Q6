import timeit
import random


import csv

MIN_MERGE = 32




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


# test0 = random.sample(range(0, 1000), 2)
# test0_3 = random.sample(range(0, 1000), 3)
# test0_4 = random.sample(range(0, 1000), 4)
# test0_5 = random.sample(range(0, 1000), 5)
# test0_7 = random.sample(range(0, 1000), 7)
# test0_8 = random.sample(range(0, 1000), 8)
# test1 = random.sample(range(0, 1000), 10)
# test2 = random.sample(range(0, 1000), 20)
# test3 = random.sample(range(0, 1000), 30)
# test4 = random.sample(range(0, 1000), 40)
# test5 = random.sample(range(0, 1000), 50)
#
# test6 = random.sample(range(0, 1000), 100)
# test7 = random.sample(range(0, 1000), 500)
# test8 = random.sample(range(0, 1000), 1000)

def comparison(lis):

    #print("list: ", lis)
    #timeit.timeit()
    start = timeit.default_timer()
    insertionSort(lis)
    end = timeit.default_timer()

    start2 = timeit.default_timer()
    mergeSort(lis, 0, len(test0)-1)
    end2 = timeit.default_timer()

    # print(start)
    # print(end)
    # print(start2)
    # print(end2)
    # print("Difference between Insertion Sort and Merge sort respectively on sorting a unsorted list with 2 values: "
    #       , end-start, "and ", end2-start2)
    # if abs(end-start) > abs(end2-start2):
    #     print("Merge Sort was faster for n ",len(lis), " : ", abs(end-start), "and ", abs(end2-start2))
    # else:
    #     print("Insertion Sort was faster for n ",len(lis), " : ", abs(end-start), "and ", abs(end2-start2))
    return [end - start, end2 - start2]
    # if end-start > end2-start2:
    #     print("Merge Sort was faster for n ",len(lis), " : ", end-start, "and ", end2-start2)
    # else:
    #     print("Insertion Sort was faster for n ",len(lis), " : ", end-start, "and ", end2-start2)


# comparison(test0)
#
# comparison(test0_3)
# comparison(test0_4)
# comparison(test0_5)
# comparison(test0_6)
# comparison(test0_7)
# comparison(test0_8)
# comparison(test0_9)
#
# comparison(test1)
# comparison(test2)
# comparison(test3)
# comparison(test4)
# comparison(test5)
# comparison(test6)
# comparison(test7)
# comparison(test8)

lis = []
lis.append(["Insertion Sort", "Merge Sort"])
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





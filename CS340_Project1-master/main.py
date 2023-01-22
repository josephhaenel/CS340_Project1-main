import matplotlib.pyplot as plt
import numpy as np
import time
import math
import random
import os

infinity = 'zzzzzzzzzz'
heapSize = 0


def insertionSort(A):  # Working

    for j in range(1, len(A)):
        key = A[j]
        i = j

        while i > 0 and A[i - 1] > key:
            A[i] = A[i - 1]
            # if i != 0:
            i = i - 1
        A[i] = key


def mergeSort(Array, start,end):
    if start < end:
        mid = int(((start + (end)) / 2))
        mergeSort(Array, start, mid)
        mergeSort(Array, mid + 1,end)
        merge(Array, start, mid, end)


def merge(A, p, q, r):  # Issue with sorting
    n1 = q - p + 1
    n2 = r - q

    L = [''] * n1
    R = [''] * n2
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L.append(infinity)
    R.append(infinity)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

# def buildMaxHeap(A):
#     heapSize = len(A)
#     for i in range(0, int(len(A) / 2)):
#         maxHeapify(A, i)

# def heapSort(A):
#     buildMaxHeap(A)
#     for i in range(0, len(A)):
#         A[1] = A[i]
#         heapSize = heapSize - 1
#         maxHeapify(A, 1)

# def maxHeapify(A, i):
#     l =

# Main function

def main():
    for j in range(2):
        if j == 0:
            sortType = 'IS'
        elif j == 1:
            sortType = 'MS'
        elif j == 2:
            sortType = 'HS'
        x1 = [0]
        y1 = [0]
        fileSize = 0
        for i in range(3):
            fileSize += 15
            fileName = 'perm' + str(fileSize) + 'K.txt'

            fileDestination = os.path.join(
                *[os.path.dirname(__file__), 'wordlists', 'PERM', fileName])

            try:

                # Reading from Files

                fileObject = open(fileDestination, "r")

                word_list = fileObject.readlines()

                fileObject.close()

                start_time = time.time()
                if j == 0:
                    insertionSort(word_list)  # Meat and Potatoes
                elif j == 1:
                    n = len(word_list) - 1
                    mergeSort(word_list, 0, n)
                end_time = time.time()
                x1.append(fileSize)
                y1.append(end_time - start_time)

                # Writing to Files

                fileName = sortType + str(fileSize) + 'K.txt'

                fileDestination = os.path.join(
                    *[os.path.dirname(__file__), 'wordlists', 'PERM_OUT', fileName])

                fileObject = open(fileDestination, 'w')

                for line in word_list:
                    fileObject.writelines(line)

                fileObject.close()

            except IOError:
                print(fileName + ' failed to open')
                
        if j == 0:
            plt.plot(x1, y1, label="Insertion Sort")
        elif j == 1:
            plt.plot(x1, y1, label="Merge Sort")
        elif j == 2:
            plt.plot(x1, y1, label="Heap Sort")
            
    plt.rcParams['figure.figsize'] = [10, 6]  # Setting size of plot

    # labels = np.array([15, 30, 45, 60, 75, 90, 100, 115, 130, 150])
    # plt.xticks(x1, labels)
    plt.xlabel('Words Sorted (thousands)')
    plt.ylabel('Time Taken (seconds)')
    plt.title("Sorting Time")
    plt.legend()
    plt.show()

main()


# testSortingList = ['date', 'apple', 'banana', 'cucumber', 'acorn', 'aaaa']
# n = len(testSortingList) - 1
# mergeSort(testSortingList, 0, n)
# print('Merge Sort:     ', testSortingList)

# testSortingList = ['date', 'apple', 'banana', 'cucumber', 'acorn', 'aaaa']

# insertionSort(testSortingList)
# print('Insertion Sort: ', testSortingList)

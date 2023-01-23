import matplotlib.pyplot as plt
import numpy as np
import time
import math
import random
import os

infinity = 'zzzzzzzzzz'
heapSize = 0

numFiles = 10


def insertionSort(A): 

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


def merge(A, p, q, r): 
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


def buildMaxHeap(A):
    heapSize = len(A)
    for i in range(int((len(A) / 2) - 1), -1, -1):
        maxHeapify(A, i, heapSize)


def heapSort(A):
    heapSize = len(A)
    buildMaxHeap(A)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapSize -= 1
        maxHeapify(A, 0, heapSize)


def maxHeapify(A, i, heapSize):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heapSize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapSize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest, heapSize)


# Main function

def main():
    for t in range(2):
        if t == 0:
            sortList = "PERM"
            sortFileType = "perm"
            sortOutFile = 'PERM_OUT'
        elif t == 1:
            sortList = "SORTED"
            sortFileType = "sorted"
            sortOutFile = 'SORT_OUT'
        for j in range(3):
            if j == 0:
                sortType = 'IS'
            elif j == 1:
                sortType = 'MS'
            elif j == 2:
                sortType = 'HS'
            x1 = [0]
            y1 = [0]
            fileSize = 0
            for i in range(numFiles):
                fileSize += 15
                fileName = sortFileType + str(fileSize) + 'K.txt'

                fileDestination = os.path.join(
                    *[os.path.dirname(__file__), 'wordlists', sortList, fileName])

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
                    elif j == 2:
                        heapSort(word_list)
                    end_time = time.time()
                    x1.append(fileSize)
                    y1.append(end_time - start_time)

                    # Writing to Files

                    fileName = sortType + str(fileSize) + 'K.txt'

                    fileDestination = os.path.join(
                        *[os.path.dirname(__file__), 'wordlists', sortOutFile, fileName])

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
        plt.rcParams["figure.autolayout"] = True

        plt.xlabel('Words Sorted (thousands)')
        plt.ylabel('Time Taken (seconds)')
        if t == 0:
            plt.title("Permuted Sorting Time")
        elif t == 1:
            plt.title("Sorted Sorting Time")
        plt.legend()
        plt.show()

        
if __name__ == '__main__':
    main()

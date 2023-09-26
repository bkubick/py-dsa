# coding: utf-8
from __future__ import annotations

from typing import Any, List, Optional


def quicksort(unsorted_list: List[Any], low: Optional[int] = None, high: Optional[int] = None) -> None:
    """ Sorts a list in-place using the quicksort algorithm.

        Args:
            unsorted_list (List[Any]): The list to sort.
    """
    if low is None:
        low = 0

    if high is None:
        high = len(unsorted_list) - 1

    if low < high:
        pivot_landing_index = _partition(unsorted_list, low, high)
        
        quicksort(unsorted_list, low, pivot_landing_index - 1)
        quicksort(unsorted_list, pivot_landing_index + 1, high)


def _partition(unsorted_list: List[Any], low: int, high: int) -> int:
    """ Partitions the list around a pivot value, and returns the index of the pivot value.

        Args:
            unsorted_list (List[Any]): The list to partition.
            low (int): The lower bound of the list to partition.
            high (int): The upper bound of the list to partition.

        Returns:
            (int) The index of the pivot value.
    """
    pivot = unsorted_list[high]
    j = low - 1
    for i in range(low, high):
        if unsorted_list[i] <= pivot:
            j += 1
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[j]
            unsorted_list[j] = temp

    j += 1
    unsorted_list[high] = unsorted_list[j]
    unsorted_list[j] = pivot

    return j


def mergesort(unsorted_list: List[Any]) -> List[Any]:
    """ Sorts a list using the mergesort algorithm.
    
        Args:
            unsorted_list (List[Any]): The list to sort.

        Returns:
            (List[Any]) The sorted list.
    """
    if len(unsorted_list) <= 1:
        return unsorted_list

    # Determine split point
    middle_index = len(unsorted_list) // 2

    # Getting the sorted subarrays
    sorted_subarray_1 = mergesort(unsorted_list[:middle_index])
    sorted_subarray_2 = mergesort(unsorted_list[middle_index:])

    sorted_array = []
    i = j = 0
    # Sorting the two subarrays until one is completely depleted
    while i < len(sorted_subarray_1) and j < len(sorted_subarray_2):
        if sorted_subarray_1[i] <= sorted_subarray_2[j]:
            sorted_array.append(sorted_subarray_1[i])
            i += 1
        else:
            sorted_array.append(sorted_subarray_2[j])
            j += 1
    
    # If subarray 2 was completeley depleted first, then finish appending elements from subarray 1
    while i < len(sorted_subarray_1):
        sorted_array.append(sorted_subarray_1[i])
        i += 1

    # If subarray 1 was completeley depleted first, then finish appending elements from subarray 2
    while j < len(sorted_subarray_2):
        sorted_array.append(sorted_subarray_2[j])
        j += 1
    
    return sorted_array


def bubble_sort(unsorted_array: List[Any]) -> None:
    """ Sort the unsorted_array in-place, using the bubble sort algorithm.

        Args:
            unsorted_array (List[Any]): The unsorted list to be sorted.
    """
    n = len(unsorted_array)

    for i in range(n):
        swapped: bool = False

        for j in range(0, len(unsorted_array) - i - 1):
            # value at j is bigger than value at j+1, then swap
            if unsorted_array[j] > unsorted_array[j + 1]:
                temp =  unsorted_array[j]
                unsorted_array[j] = unsorted_array[j + 1]
                unsorted_array[j + 1] = temp
                swapped = True

        # Once we have no more swaps, then the array is fully sorted
        if swapped is False:
            break


def selection_sort(unsorted_array: List[Any]) -> None:
    """ Sort the unsorted_array in-place, using the selection sort algorithm.
    
        Args:
            unsorted_array (List[Any]): The unsorted list to be sorted.
    """
    n = len(unsorted_array)

    for i in range(n):
        # Setting the min value to the current index, so if nothing is larger, then it swaps with itself
        min_value_index = i

        # Searching through the remaining unsorted elements to find the index of the next smallest value
        for j in range(i + 1, n):
            if unsorted_array[j] < unsorted_array[min_value_index]:
                min_value_index = j

        # Swapping the elements
        temp = unsorted_array[i]
        unsorted_array[i] = unsorted_array[min_value_index]
        unsorted_array[min_value_index] = temp


def insertion_sort(unsorted_array: List[Any]) -> None:
    """ Sort the unsorted_array in-place, using the insertion sort algorithm.

        Args:
            unsorted_array (List[Any]): The unsorted list to be sorted.
    """
    n = len(unsorted_array)

    for i in range(1, n):
        # Storing the current value to compare against
        current_value = unsorted_array[i]
        
        j = i - 1
        # Going backwards through the already sorted array, to put the current_value in the correct spot
        # If j < 0, then its at the beginning of the array, so the value is the minimum so far (index 0)
        # If current_value > unsorted_array[j], then it is the highest value of the sorted values so far
        while current_value < unsorted_array[j] and j >= 0:
            unsorted_array[j + 1] = unsorted_array[j]
            j -= 1

        # Putting the current_value in it's correct location of the already sorted array.
        unsorted_array[j + 1] = current_value

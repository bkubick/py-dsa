# coding: utf-8
from __future__ import annotations

from typing import Any, List, Optional


def binary_search(sorted_array: List[Any],
                  value: Any,
                  left_index: Optional[int] = None,
                  right_index: Optional[int] = None) -> int:
    """ Searches a sorted list for a value using the binary search algorithm.

        Args:
            sorted_array (List[Any]): The sorted list to search.
            value (Any): The value to search for.
            left_index (Optional[int]): The left index of the list to search.
            right_index (Optional[int]): The right index of the list to search.

        Returns:
            (int) The index of the value in the list, or -1 if the value is not in the list.
    """
    # When the left or right index are not set, need to set these to the edge indices of the list
    if left_index is None:
        left_index = 0
    if right_index is None:
        right_index = len(sorted_array) - 1

    # When left index exceeds the right index, then there are no more locations in the array to search.
    if left_index > right_index:
        return -1

    # Need to get the middle index between the left_index and right_index
    mid_index = left_index + (right_index - left_index) // 2

    if sorted_array[mid_index] > value:
        return binary_search(sorted_array=sorted_array, value=value, left_index=left_index, right_index=mid_index - 1)
    elif sorted_array[mid_index] < value:
        return binary_search(sorted_array=sorted_array, value=value, left_index=mid_index + 1, right_index=right_index)
    else:
        return mid_index

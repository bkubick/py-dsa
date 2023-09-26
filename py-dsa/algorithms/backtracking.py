# coding: utf-8
from __future__ import annotations

import typing

T = typing.TypeVar('T')


def permutations(values: typing.List[T]) -> typing.List[typing.List[T]]:
    """ Returns all permutations of a list of values.
    
        Args:
            values (typing.List[T]): The list of numbers to permutate.

        Returns:
            (typing.List[typing.List[T]]) A list of all permutations of the list of values.
    """
    permutations = []

    def permutate(permutations: typing.List[typing.List[T]],
                  remaining_nums: typing.List[T],
                  current_permutation: typing.List[T]):
        if len(remaining_nums) == 0:
            permutations.append(current_permutation)

        for i in range(len(remaining_nums)):
            nums_to_permutate = remaining_nums[:i] + remaining_nums[i+1:]
            permutation = current_permutation + [remaining_nums[i]]
            permutate(permutations, nums_to_permutate, permutation)

    permutate(permutations, values, [])

    return permutations


def subsets(values: typing.List[T]) -> typing.List[typing.List[T]]:
    """ Returns all subsets of a list of values.
    
        Args:
            values (typing.List[T]): The list of numbers to get subsets of.

        Returns:
            (typing.List[typing.List[T]]) A list of all subsets of the list of numbers.
    """
    # Deduping because a set is deduped by definition.
    values = list[set(values)]
    unique_sets = []

    def backtrack(current_set: typing.List[T], remaining_vals: typing.List[T]):
        if current_set not in unique_sets:
            unique_sets.append(current_set)

        for i in range(len(remaining_vals)):
            new_set = current_set + [remaining_vals[i]]
            backtrack(new_set, remaining_vals[i+1:])

    backtrack([], values)

    return unique_sets

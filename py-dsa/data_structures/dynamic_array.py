# coding: utf-8
from __future__ import annotations

import typing

T = typing.TypeVar('T')


class DynamicArray:
    """ A dynamic array implementation.
    
        Attributes:
            capacity (int): The capacity of the array.
        
        Private Attributes:
            _length (int): The length of the array.
            _array (List[Any]): The array.
        
        Methods:
            get: Gets the value at the given index.
            insert: Inserts a value at the given index.
            pushback: Pushes a value to the back of the array.
            popback: Pops a value from the back of the array.
            resize: Resizes the array to double its current capacity.
            get_size: Gets the size of the array.
            get_capacity: Gets the capacity of the array.
    """

    def __init__(self, capacity: int):
        """ Initializes the dynamic array.
        
            Args:
                capacity (int): The capacity of the array.
        """
        self.capacity = capacity
        self._length = 0
        self._array: typing.List[T] = [0] * self.capacity


    def get(self, i: int) -> T:
        """ Gets the value at the given index.
        
            Args:
                i (int): The index to get the value at.
            
            Returns:
                (T) The value at the given index.
        """
        return self._array[i]

    def insert(self, i: int, n: T) -> None:
        """ Inserts a value at the given index.
        
            Args:
                i (int): The index to insert the value at.
                n (T): The value to insert.
        """
        self._array[i] = n

    def pushback(self, n: T) -> None:
        """ Pushes a value to the back of the array.
        
            Args:
                n (T): The value to push to the back of the array.
        """
        if self._length == self.capacity:
            self.resize()

        self._array[self._length] = n
        self._length += 1

    def popback(self) -> T:
        """ Pops a value from the back of the array.
        
            Returns:
                (T) The value popped from the back of the array.
        
            Raises:
                IndexError: If the array is empty.
        """
        if self._length > 0:
            self._length -= 1

        return self._array[self._length]

    def resize(self) -> None:
        """ Resizes the array to double its current capacity.
        """
        self._array += [0] * self.capacity
        self.capacity *= 2

    def get_size(self) -> int:
        """ Gets the size of the array.
        
            Returns:
                (int) The size of the array.
        """
        return self._length
    
    def get_capacity(self) -> int:
        """ Gets the capacity of the array.
        
            Returns:
                (int) The capacity of the array.
        """
        return self.capacity

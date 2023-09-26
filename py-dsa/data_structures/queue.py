# coding: utf-8

from __future__ import annotations

from typing import Generic, TypeVar


__all__ = [
    'FrontMiddleBackQueue',
]


T = TypeVar('T')


class FrontMiddleBackQueue(Generic[T]):
    """ A queue that supports adding and removing elements from the front, middle, and back of the queue.

        Attributes:
            size (int): The size of the queue.

        Private Attributes:
            _queue (List[T]): The queue.
            _middle_index (int): The middle index of the queue.
        
        Methods:
            is_empty: Returns whether the queue is empty.
            push_front: Adds a value to the front of the queue.
            push_middle: Adds a value to the middle of the queue.
            push_back: Adds a value to the back of the queue.
            pop_front: Removes and returns the first element of the queue.
            pop_middle: Removes and returns the middle element of the queue.
            pop_back: Removes and returns the last element of the queue.
    """

    def __init__(self):
        self._queue = []

    @property
    def size(self) -> int:
        """ Returns the size of the queue. """
        return len(self._queue)

    @property
    def _middle_index(self) -> int:
        """ Returns the middle index of the queue. """
        return int(self.size // 2)

    def is_empty(self) -> bool:
        """ Returns whether the queue is empty.
        
            Returns:
                (bool) Whether the queue is empty.
        """
        return self.size == 0

    def push_front(self, val: T) -> None:
        """ Adds a value to the front of the queue.
        
            Args:
                val (T): The value to add to the front of the queue.
        """
        self._queue.insert(0, val)

    def push_middle(self, val: T) -> None:
        """ Adds a value to the middle of the queue.
        
            Args:
                val (T): The value to add to the middle of the queue.
        """
        self._queue.insert(self._middle_index, val)

    def push_back(self, val: T) -> None:
        """ Adds a value to the back of the queue.
        
            Args:
                val (T): The value to add to the back of the queue.
        """
        self._queue.append(val)

    def pop_front(self) -> T:
        """ Removes and returns the first element of the queue.

            Raises:
                IndexError: If the queue is empty.
        
            Returns:
                (T) The first element of the queue.
        """
        if self.is_empty():
            raise IndexError('Queue is empty.')

        return self._queue.pop(0)

    def pop_middle(self) -> T:
        """ Removes and returns the middle element of the queue.

            Raises:
                IndexError: If the queue is empty.

            Returns:
                (T) The middle element of the queue.
        """
        if self.is_empty():
            raise IndexError('Queue is empty.')

        if self.size % 2 == 0:
            return self._queue.pop(self._middle_index - 1)

        return self._queue.pop(self._middle_index)

    def pop_back(self) -> T:
        """ Removes and returns the last element of the queue.

            Raises:
                IndexError: If the queue is empty.

            Returns:
                (T) The last element of the queue.
        """
        if self.is_empty():
            raise IndexError('Queue is empty.')

        return self._queue.pop(-1)

    def __str__(self) -> str:
        return str(self._queue)

    def __repr__(self) -> str:
        return f'FrontMiddleBackQueue({self._queue})'
    
    def __len__(self) -> int:
        return self.size

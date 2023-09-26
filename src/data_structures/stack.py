# coding: utf-8

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, List


__all__ = [
    'MinStack',
    'MaxStack',
]

T = TypeVar('T')


class _StackBase(ABC):
    """ An abstract stack class.

        Methods:
            push: Pushes a value to the stack.
            pop: Pops the top value from the stack.
            top: Gets the top value in the stack.
    """

    @abstractmethod
    def push(self, val: T) -> None:
        """ Pushes a value to the stack.

            Args:
                val (T): The value to push to the stack.
        """
        pass

    @abstractmethod
    def pop(self) -> None:
        """ Pops the top value from the stack.
        """
        pass

    @abstractmethod
    def top(self) -> T:
        """ Gets the top value in the stack.
        
            Returns:
                (T) The top value in the stack.
        """
        pass


class MinStack(_StackBase):
    """ A stack that supports getting the minimum value in O(1) time.

        Private Attributes:
            _stack (List[T]): The stack.
            _min_stack (List[T]): The stack of minimum values.
        
        Methods:
            push: Pushes a value to the stack.
            pop: Pops the top value from the stack.
            top: Gets the top value in the stack.
            get_min: Gets the minimum value in the stack.
    """

    def __init__(self):
        self._stack: List[T] = []
        self._min_stack: List[T] = []
    
    def push(self, val: T) -> None:
        """ Pushes a value to the stack.

            Args:
                val (T): The value to push to the stack.
        """
        self._stack.append(val)
        if len(self._min_stack) == 0 or val <= self._min_stack[-1]:
            self._min_stack.append(val)
    
    def pop(self) -> None:
        """ Pops the top value from the stack.
        """
        if self._stack[-1] == self._min_stack[-1]:
            self._min_stack.pop()
        self._stack.pop()
    
    def top(self) -> T:
        """ Gets the top value in the stack.
        
            Returns:
                (T) The top value in the stack.
        """
        return self._stack[-1]
    
    def get_min(self) -> T:
        """ Gets the minimum value in the stack.

            Returns:
                (T) The minimum value in the stack.
        """
        return self._min_stack[-1]

    def __repr__(self) -> str:
        """ Representation of MinStack. """
        return f"MinStack: {self._stack}"


class MaxStack(_StackBase):
    """ A stack that supports getting the maximum value in O(1) time.
    
        Private Attributes:
            _stack (List[T]): The stack.
            _max_stack (List[T]): The stack of maximum values.
        
        Methods:
            push: Pushes a value to the stack.
            pop: Pops the top value from the stack.
            top: Gets the top value in the stack.
            get_max: Gets the maximum value in the stack.
    """

    def __init__(self) -> None:
        self._stack = []
        self._max_stack = []
    
    def push(self, val: T) -> None:
        """ Pushes a value to the stack.
        
            Args:
                val (T): The value to push to the stack.
        """
        self._stack.append(val)
        if len(self._max_stack) == 0 or val >= self._max_stack[-1]:
            self._max_stack.append(val)
    
    def pop(self) -> None:
        """ Pops the top value from the stack.
        """
        if self._stack[-1] == self._max_stack[-1]:
            self._max_stack.pop()
        self._stack.pop()
    
    def top(self) -> T:
        """ Gets the top value in the stack.
        
            Returns:
                (T) The top value in the stack.
        """
        return self._stack[-1]
    
    def get_max(self) -> T:
        """ Gets the maximum value in the stack.
        
            Returns:
                (T) The maximum value in the stack.
        """
        return self._max_stack[-1]

    def __repr__(self) -> str:
        """ Representation of MaxStack. """
        return f"MaxStack: {self._stack}"

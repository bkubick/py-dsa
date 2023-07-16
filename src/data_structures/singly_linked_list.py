from __future__ import annotations

from typing import Iterable, Iterator, List, Optional, Generic, TypeVar

T = TypeVar('T')


class SingleLinkedListIterator(Generic[T], Iterator):
    """ Iterator for SinglyLinkedList.
    
        Attributes:
            _node (Optional[SinglyLinkedList.Node]): Current node in iteration.
    """

    _node: Optional[SinglyLinkedList.Node]

    def __init__(self, start_node: Optional[SinglyLinkedList.Node]):
        self._node = start_node
    
    def __next__(self) -> T:
        """ Get next value in iteration.
        
            Returns:
                T: Next value in iteration.
        """
        if self._node is None:
            raise StopIteration

        ret = self._node.value
        self._node = self._node.next

        return ret
    
    def __iter__(self) -> SingleLinkedListIterator[T]:
        """ Iterator for SinglyLinkedList. """
        return self


class SinglyLinkedList(Generic[T], Iterable):
    """ Singly linked list implementation.
    
        Attributes:
            _head (Optional[SinglyLinkedList.Node]): Starting node of list.
            _tail (Optional[SinglyLinkedList.Node]): Ending node of list.
            _size (int): Size of list.
    """
    
    class Node:
        """ Node class for SinglyLinkedList.
        
            Attributes:
                value (T): Value of node.
                next (Optional[SinglyLinkedList.Node]): Next node in list.
        """
        value: T
        next: Optional[SinglyLinkedList.Node]

        def __init__(self, value: T):
            self.value = value
            self.next = None
        
        def __repr__(self) -> str:
            """ Representation of Node. """
            return f'<Node value={self.value} next={self.next.value if self.next else None}>'

    _head: Optional[Node]
    _tail: Optional[Node]
    _size: int

    def __init__(self, value: Optional[Iterable[T]] = None):
        self._head = self._tail = None
        self._size = 0

        if value is not None:
            self._link_list(value)

    def __str__(self) -> str:
        """ String representation of SinglyLinkedList. """
        return str(self.to_list())

    def __repr__(self) -> str:
        """ Representation of SinglyLinkedList. """
        return f'SinglyLinkedList ({self.__str__()})'

    def __len__(self) -> int:
        """ Length of SinglyLinkedList. """
        return self._size

    def __iter__(self) -> SingleLinkedListIterator[T]:
        """ Iterator for SinglyLinkedList. """
        return SingleLinkedListIterator(self._head)

    def _link_list(self, value: Iterable[T]) -> None:
        """ Link list of values together.
        
            Args:
                value (Iterable[T]): List of values to link together.
        """
        prev_node: Optional[SinglyLinkedList.Node] = None
        for val in value:
            new_node: SinglyLinkedList.Node = SinglyLinkedList.Node(val)

            if prev_node is not None:
                prev_node.next = new_node
            else:
                self._head = new_node

            self._size += 1
            prev_node = new_node
        
        self._tail = prev_node

    def to_list(self) -> List[T]:
        """ Convert linked list to python list.

            Returns:
                List[T]: Python list representation of linked list.
        """
        ret: List[T] = []

        node = self._head
        while node is not None:
            ret.append(node.value)
            node = node.next

        return ret

    def append(self, value: T) -> None:
        """ Append value to end of list.
        
            Args:
                value (T): Value to append to end of list.
        """
        new_node = SinglyLinkedList.Node(value=value)
        
        if self._head is None and self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1

    def insert(self, value: T) -> None:
        """  Insert value at start of list
         
            Args:
                value (T): Value to insert at start of list.
        """
        new_node = SinglyLinkedList.Node(value=value)

        if self._head is None:
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        
        self._size += 1

    def pop(self) -> Optional[T]:
        """ Remove and return last element in list.
        
            Returns:
                T: Value of last element in list, or None if list is empty.
        """
        if self._tail is None:
            return None

        ret = self._tail.value

        node = self._head
        while node is not None:
            if node == self._tail and node == self._head:
                self._head = self._tail = None
                break
            elif node.next == self._tail:
                node.next = None
                self._tail = node
                break

            node = node.next
        
        self._size -= 1

        return ret

    def remove(self, value: T) -> T:
        """ Remove first occurence of value in list
        
            Args:
                value (T): Value to remove
            
            Raises:
                IndexError: If value is not in list
            
            Returns:
                T: Value removed
        """
        if self._head is None:
            raise IndexError(f'No element of value {value}')

        node = self._head
        prev_node: Optional[SinglyLinkedList.Node] = None
        while node is not None:
            if node.value == value:
                # Node found is not starting node and not ending node
                if prev_node is not None and node.next is not None:
                    prev_node.next = node.next
                # Node found is starting node not end node
                elif prev_node is None and node.next is not None:
                    self._head = node.next
                # Node is end node and not starting node
                elif prev_node is not None and node.next is None:
                    self._tail = prev_node
                    self._tail.next = None
                # Node is starting and ending node
                elif prev_node is None and node.next is None:
                    self._head = self._tail = None

                break
            elif node.next is None:
                raise AttributeError(f'No node found for value {value}')

            prev_node = node
            node = node.next

        self._size -= 1

    def get(self, index: int) -> T:
        """ Get value at index
        
            Args:
                index (int): Index of value to get

            Raises:
                IndexError: If index is out of bounds

            Returns:
                T: Value at index
        """
        if self._head is None:
            raise IndexError(f'Index not accessible')
        elif index >= self._size:
            raise IndexError(f'Index not accessible')

        node = self._head
        for _ in range(index):
            node = node.next
        
        return node.value

    def count(self, value: T) -> int:
        """ Count number of times value appears in list 
        
            Args:
                value (T): Value to count
            
            Returns:
                int: Number of times value appears in list
        """
        count: int = 0

        node = self._head
        while node is not None:
            if node.value == value:
                count += 1

            node = node.next
        
        return count

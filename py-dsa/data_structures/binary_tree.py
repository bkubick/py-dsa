from __future__ import annotations

from typing import Generic, List, Optional, Set, TypeVar


T = TypeVar('T')


class BinaryTree(Generic[T]):
    """ Binary tree implementation.
    
        Attributes:
            _root (Optional[BinaryTree.Node]): Root node of tree.
    """

    class Node:
        """ Node class for BinaryTree.

            Attributes:
                value (T): Value of node.
                left (Optional[BinaryTree.Node]): Left node of current node.
                right (Optional[BinaryTree.Node]): Right node of current node.
        """
        value: T
        left: Optional[BinaryTree.Node]
        right: Optional[BinaryTree.Node]

        def __init__(self, value: BinaryTree.Node) -> None:
            self.value = value
            self.left = None
            self.right = None

        def __repr__(self) -> str:
            """ String representation of node. """
            left = self.left.value if self.left else None
            right = self.right.value if self.right else None
            return f'<Node value={self.value} left={left} right={right}>'       

    _root: Optional[Node]

    def __init__(self):
        self._root = None

    def __str__(self) -> str:
        """ String representation of BinaryTree. """
        return f'BinaryTree ({self.__repr__()})'

    def __repr__(self) -> str:
        """ String representation of BinaryTree. """
        return str(self.in_order_traversal())

    def _insert(self, value: T, node: BinaryTree.Node) -> None:
        """ Insert value into tree helper function.
        
            Args:
                value (T): Value to insert into tree.
                node (BinaryTree.Node): Node to insert value into.
        """
        if node.value >= value:
            if node.left is None:
                node.left = BinaryTree.Node(value)
            else:
                self._insert(value, node=node.left)
        else:
            if node.right is None:
                node.right = BinaryTree.Node(value)
            else:
                self._insert(value, node=node.right)

    def insert(self, value: T) -> None:
        """ Insert value into tree.
        
            Args:
                value (T): Value to insert into tree.
        """
        if self._root is None:
            self._root = BinaryTree.Node(value)
        else:
            self._insert(value, self._root)

    def _in_order_traversal(self, node: Optional[BinaryTree.Node]) -> List[T]:
        """ In order traversal helper function.
        
            Args:
                node (Optional[BinaryTree.Node]): Node to traverse from.
        """
        if node is None:
            return []

        traversed_tree = []

        traversed_tree.extend(self._in_order_traversal(node.left))
        traversed_tree.append(node.value)
        traversed_tree.extend(self._in_order_traversal(node.right))

        return traversed_tree

    def in_order_traversal(self) -> List[T]:
        """ In order traversal of tree.

            Example:
                >>> tree = BinaryTree()
                >>> tree.insert(5)
                >>> tree.insert(3)
                >>> tree.insert(7)
                >>> tree.insert(2)
                >>> tree.insert(4)
                >>> tree.insert(6)
                >>> tree.insert(8)
                >>> tree.in_order_traversal()
                [2, 3, 4, 5, 6, 7, 8]

            Returns:
                List[T]: In order traversal of tree.
        """
        return self._in_order_traversal(self._root)

    def _pre_order_traversal(self, node: Optional[BinaryTree.Node]) -> List[T]:
        """ Pre order traversal helper function.

            Args:
                node (Optional[BinaryTree.Node]): Node to traverse from.
        """
        if node is None:
            return []

        traversed_tree = [node.value]
        traversed_tree.extend(self._pre_order_traversal(node.left))
        traversed_tree.extend(self._pre_order_traversal(node.right))

        return traversed_tree

    def pre_order_traversal(self) -> List[T]:
        """ Pre order traversal of tree.

            Example:
                >>> tree = BinaryTree()
                >>> tree.insert(5)
                >>> tree.insert(3)
                >>> tree.insert(7)
                >>> tree.insert(2)
                >>> tree.insert(4)
                >>> tree.insert(6)
                >>> tree.insert(8)
                >>> tree.pre_order_traversal()
                [5, 3, 2, 4, 7, 6, 8]

            Returns:
                List[T]: Pre order traversal of tree.    
        """
        return self._pre_order_traversal(self._root)

    def _post_order_traversal(self, node: Optional[BinaryTree.Node]) -> List[T]:
        """ Post order traversal helper function.
        
            Args:
                node (Optional[BinaryTree.Node]): Node to traverse from.
        """
        if node is None:
            return []

        traversed_tree = []

        traversed_tree.extend(self._post_order_traversal(node.left))
        traversed_tree.extend(self._post_order_traversal(node.right))
        traversed_tree.append(node.value)

        return traversed_tree

    def post_order_traversal(self) -> List[T]:    
        """ Post order traversal of tree.

            Example:
                >>> tree = BinaryTree()
                >>> tree.insert(5)
                >>> tree.insert(3)
                >>> tree.insert(7)
                >>> tree.insert(2)
                >>> tree.insert(4)
                >>> tree.insert(6)
                >>> tree.insert(8)
                >>> tree.post_order_traversal()
                [2, 4, 3, 6, 8, 7, 5]
        """
        return self._post_order_traversal(self._root)

    def breadth_first_search(self, log_visit_step: bool = False) -> List[T]:
        """ Breadth first search of tree.

            Example:
                >>> tree = BinaryTree()
                >>> tree.insert(5)
                >>> tree.insert(3)
                >>> tree.insert(7)
                >>> tree.insert(2)
                >>> tree.insert(4)
                >>> tree.insert(6)
                >>> tree.insert(8)
                >>> tree.breadth_first_search()
                [5, 3, 7, 2, 4, 6, 8]
            
            Args:
                log_visit_step (bool): Whether or not to log the current node being visited.
            
            Returns:
                List[T]: Breadth first search of tree.
        """
        visited: Set[BinaryTree.Node] = set()
        queue: List[BinaryTree.Node] = []

        queue.append(self._root)
        while len(queue) > 0:
            current_location = queue.pop(0)
            visited.add(current_location)

            if log_visit_step:
                print('Currently At: ', current_location)

            if current_location.left is not None and current_location.left not in visited and current_location.left not in queue:
                queue.append(current_location.left)
            
            if current_location.right is not None and current_location.right not in visited and current_location.right not in queue:
                queue.append(current_location.right)

        return [node.value for node in visited]

    def depth_first_search(self, log_visit_step: bool = False) -> List[T]:
        """ Depth first search of tree.

            Example:
                >>> tree = BinaryTree()
                >>> tree.insert(5)
                >>> tree.insert(3)
                >>> tree.insert(7)
                >>> tree.insert(2)
                >>> tree.insert(4)
                >>> tree.insert(6)
                >>> tree.insert(8)
                >>> tree.depth_first_search()
                [5, 3, 7, 2, 4, 6, 8]

            Args:
                log_visit_step (bool): Whether or not to log the current node being visited.
                
            Returns:
                List[T]: Depth first search of tree.
        """
        visited: Set[BinaryTree.Node] = set()
        stack: List[BinaryTree.Node] = []

        stack.append(self._root)
        while len(stack) > 0:
            current_location = stack.pop(-1)
            visited.add(current_location)

            if log_visit_step:
                print('Currently At: ', current_location)

            if current_location.left is not None and current_location.left not in visited and current_location.left not in stack:
                stack.append(current_location.left)
            
            if current_location.right is not None and current_location.right not in visited and current_location.right not in stack:
                stack.append(current_location.right)

        return [node.value for node in visited]

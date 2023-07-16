from __future__ import annotations

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    """ Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # When the list is empty, or all items in the list are None
        if len(lists) == 0 or not all(lists):
            return None

        # Creating new list
        copied_lists = lists.copy()

        root_node = node = None
        while any(copied_lists):
            # initializing the min node as None so it can be determined
            lowest_min_node_index = None
            # Need to go through each linked list, and check the front most value
            for j in range(len(copied_lists)):
                # When the linked list is at it's end, the value in the original list is None.
                if copied_lists[j] is None:
                    continue
                # Setting the lowest_min_node_index for the first time
                elif lowest_min_node_index is None:
                    lowest_min_node_index = j

                # Go through linked list node
                if copied_lists[j].val < copied_lists[lowest_min_node_index].val:
                    lowest_min_node_index = j

            if node is None:
                # The first node created also needs to set the root_node
                node = ListNode(copied_lists[lowest_min_node_index].val)
                root_node = node
            else:
                node.next = ListNode(copied_lists[lowest_min_node_index].val)
                node = node.next

            # Going to the next node for the value in the list with the minimum value
            copied_lists[lowest_min_node_index] = copied_lists[lowest_min_node_index].next
        
        return root_node

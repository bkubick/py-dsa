# coding: utf-8

from __future__ import annotations

from collections import defaultdict


__all__ = ['Trie']


class _TrieNode(defaultdict):
    """ A node in a trie.

        Attributes:
            is_word (bool): Whether or not the node represents a word.
    """
    is_word: bool

    def __init__(self):
        super().__init__(_TrieNode)
        self.is_word = False


class Trie:
    """ A trie implementation.

        Attributes:
            _nodes (Dict[str, dict]): The nodes in the trie.
        
        Methods:
            insert: Inserts a word into the trie.
            search: Searches for a word in the trie.
            starts_with: Searches for a prefix in the trie.
    """

    def __init__(self):
        self._nodes: _TrieNode = _TrieNode()

    def insert(self, word: str) -> None:
        """ Inserts a word into the trie.

            Args:
                word (str): The word to insert.
        """
        current_mapping: _TrieNode = self._nodes
        for letter in word:
            current_mapping = current_mapping[letter]

        current_mapping.is_word = True

    def search(self, word: str) -> bool:
        """ Searches for a word in the trie.
        
            Args:
                word (str): The word to search for.
        
            Returns:
                (bool) Whether or not the word is in the trie.
        """
        current_mapping: _TrieNode = self._nodes

        for letter in word:
            if letter not in current_mapping:
                return False
            
            current_mapping = current_mapping[letter]

        return current_mapping.is_word

    def starts_with(self, prefix: str) -> bool:
        """ Searches for a prefix in the trie.
        
            Args:
                prefix (str): The prefix to search for.
            
            Returns:
                (bool) Whether or not the prefix is in the trie.
        """
        current_mapping: _TrieNode = self._nodes

        for letter in prefix:
            if letter not in current_mapping:
                return False
            
            current_mapping = current_mapping[letter]

        return True

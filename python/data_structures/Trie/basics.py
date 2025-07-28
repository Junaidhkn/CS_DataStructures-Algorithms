# ------------------------ TRIE (PREFIX TREE) NOTES ------------------------

# Trie (pronounced "try" also known as Retrieval or Prefix Tree) is a tree_traversal-like data structure that stores a dynamic set of strings, where keys are usually words composed of characters.

# It is mainly used for:
# - Efficient retrieval of strings
# - Auto-complete systems
# - Spell-checking
# - Prefix-based search
# - Dictionary implementations

# ------------------------ TRIE TERMINOLOGY ------------------------

# - Each node represents a character of a word.
# - Root node is empty (represents no character).
# - Edges represent connections between characters.
# - A boolean flag `is_end_of_word` is usually used to mark the end of a valid word.
# - All descendants of a node share the same prefix.

# ------------------------ TRIE STRUCTURE EXAMPLE ------------------------

# To insert the words: "cat", "cap", "can"

#        (root)
#         /
#       'c'
#        |
#       'a'
#     /  |  \
#   't' 'p' 'n'
#  [✔] [✔] [✔]   ← is_end_of_word is True at these nodes

# ------------------------ TRIE OPERATIONS ------------------------

# 1. Insertion:
# - Start from the root.
# - For each character in the word:
#     - If the character does not exist as a child, create a new node.
#     - Move to the child node.
# - After the last character, mark the node as end of a word.
# - Time Complexity: O(L), where L = length of the word

# 2. Search:
# - Start from the root.
# - For each character in the word:
#     - If the character is not found among the children, return False.
#     - Move to the child node.
# - After the last character, return the value of is_end_of_word.
# - Time Complexity: O(L)

# 3. StartsWith (Prefix search):
# - Same as search, but return True after traversing all characters of the prefix.
# - Time Complexity: O(L)

# ------------------------ TRIE SPACE COMPLEXITY ------------------------

# Space Complexity: O(N * L)
# - N = number of words
# - L = average length of words
# - Each node can have up to 26 children (for lowercase English letters)

# In practice, Tries can use more space than HashMaps but offer faster prefix search.

# ------------------------ TRIE ADVANTAGES ------------------------

# ✅ Faster prefix lookups compared to HashMaps
# ✅ Prevents unnecessary comparisons during search
# ✅ Supports alphabetical traversal (can be used for lexicographic sorting)

# ------------------------ TRIE DISADVANTAGES ------------------------

# ❌ High memory usage (especially with sparse data)
# ❌ Implementation is more complex than simple maps or sets

# ------------------------ WHEN TO USE TRIES ------------------------

# ✅ Large dataset of strings with common prefixes
# ✅ Applications that require prefix-based searching or auto-completion
# ✅ Word games, dictionaries, and IP routing (bitwise tries)

# ------------------------ ALTERNATIVES ------------------------

# - HashMap/Dictionary: Faster insert/search, but slower prefix search
# - Ternary Search Tree: Hybrid of BST and Trie (space efficient)
# - Radix Tree / Compressed Trie: Reduces space by collapsing single-child chains

# -------------------------------------------------------------------------
































class TrieNode:
    def __init__(self):
        self.children = {}  
        self.terminal = False

def trie_insert(root, word):
    if root[0] is None:
        root[0] = TrieNode()
    current = root[0]
    for char in word:
        if char not in current.children:
            current.children[char] = TrieNode()
        current = current.children[char]
    current.terminal = True

def autocomplete_recursive(node, prefix):
    """
    Recursively collects words starting from this node.
    """
    results = []
    if node.terminal:
        results.append(prefix)
    for char, child in node.children.items():
        results.extend(autocomplete_recursive(child, prefix + char))
    return results

def autocomplete(root, prefix):
    if root[0] is None:
        return []
    current = root[0]
    for char in prefix:
        if char not in current.children:
            return []
        current = current.children[char]
    return autocomplete_recursive(current, prefix)


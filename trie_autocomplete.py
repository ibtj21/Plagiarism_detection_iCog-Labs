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
    If node.terminal is True → current prefix is a complete word, add to results.
    Recursively explore all children and append characters to the prefix.
    """
    results = []
    if node.terminal:
        results.append(prefix)
    for char, child in node.children.items():
        results.extend(autocomplete_recursive(child, prefix + char)) # makes sure all words from all branches get collected into one final list
    return results

def autocomplete(root, prefix):
    """Finds the Trie node that matches the given prefix.
    If prefix path exists → calls autocomplete_recursive from that node.
    Returns a list of all words that start with the prefix."""
    if root[0] is None:
        return []
    current = root[0]
    for char in prefix:
        if char not in current.children:
            return []
        current = current.children[char]
    return autocomplete_recursive(current, prefix)


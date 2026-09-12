class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(root,index):
            current = root
            for i in range(index,len(word)):
                char = word[i]
                if char == ".":
                    for child in current.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]

            return current.endOfWord
        return dfs(self.root,0)        
# TODO: Add comments tomorrow. Use a trie for addWord. For search, when we hit ".", use DFS/backtracking to try every possible path in the trie.
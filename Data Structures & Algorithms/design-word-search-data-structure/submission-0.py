class TrieNode:
    def __init__(self):
        self.children = {}  # Empty hash map
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # Empty Node

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]

        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                if word[i] == ".":
                    #Deal with it
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                elif word[i] not in curr.children:
                    return False
                else:
                    #word exiss and it's a reg character:
                    curr = curr.children[word[i]]
            
            return curr.endOfWord
        return dfs(0,self.root)
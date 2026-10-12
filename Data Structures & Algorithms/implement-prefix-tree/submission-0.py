class TrieNode:
    def __init__(self):
        self.children = {}  # Hashmap
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()  # root is empty, define the tree here.

    def insert(self, word: str) -> None:
        curr = self.root

        # Iterate character by character in the word
        for letter in word:
            if letter not in curr.children:  # If it doesn't exist add it
                curr.children[letter] = TrieNode()
            # If curr exists then set curr to that child
            curr = curr.children[letter]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return curr.endOfWord  # Need to make sure it isn't prefix of another word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return True  # Need to make sure it isn't prefix of another word

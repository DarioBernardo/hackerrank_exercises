def dfs(w: str, node: dict) -> bool:
    if len(w) == 1:
        if w != ".":
            return w in node and "IS_END" in node[w]
        else:
            for letter, children in node.items():
                if isinstance(children, dict) and "IS_END" in children:
                    return True
            return False

    c = w[0]
    if c == ".":
        children_branches = []
        for letter_dict in node.values():
            if isinstance(letter_dict, dict):
                children_branches.append(dfs(w[1:], letter_dict))

        return any(children_branches)
    else:
        if isinstance(node, dict) and c in node:
            return dfs(w[1:], node[c])

    return False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def addWord(self, word: str) -> None:
        if word is None or word == "":
            return

        current_level = self.root

        for c in word:
            level = current_level.get(c, dict())
            current_level[c] = level
            current_level = level

        current_level["IS_END"] = True

    def search(self, word: str) -> bool:
        if word is None:
            return False

        return dfs(word, self.root)


word_dictionary = WordDictionary()
word_dictionary.addWord("bad")
word_dictionary.addWord("dad")
word_dictionary.addWord("mad")
assert not word_dictionary.search("pad")
assert word_dictionary.search("bad")
assert word_dictionary.search(".ad")
assert word_dictionary.search("b..")

#["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
#[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]

word_dictionary = WordDictionary()
word_dictionary.addWord("a")
word_dictionary.addWord("a")
assert word_dictionary.search(".")
assert word_dictionary.search("a")
assert not word_dictionary.search("aa")
assert word_dictionary.search("a")
assert not word_dictionary.search("a.")
assert not word_dictionary.search(".a")

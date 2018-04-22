'''
Trie Implementation
1. Create a Trie data structure
2. Check a word exists in the trie structure
3. Search the prefix and output the words lexicographically
Uses
- Prefix based search
- Sort Lexicographically
'''
import re
class Trie_Node(object):
    def __init__(self,label=None,data=None):
        self.children=dict()
        self.label=label
        self.data=data

    def add_child(self, key, data=None):
        if not isinstance(key, Trie_Node):
            self.children[key]=Trie_Node(key, data)
        else:
            self.children[key.label]=key

    def __getitem__(self, key):
        return self.children[key]

class Trie(object):
    def __init__(self):
        self.root=Trie_Node()

    def __getitem__(self,key):
        return self.root.children[key]

    def insert(self, word):
        '''
        :param word:
        :return:
        '''
        current_node = self.root
        word_finished = True

        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break

        # For ever new letter, create a new child node
        if not word_finished:
            while i < len(word):
                current_node.add_child(word[i])
                current_node = current_node.children[word[i]]
                i += 1

        # Let's store the full word at the end node always
        current_node.data = word

    def has_word(self,word):
        '''
        :param word:
        :return: True/False
        '''
        if word in ['',None]:
            return False
        curr=self.root
        present=True
        for letter in word:
            if letter in curr.children:
                curr=curr.children[letter]
            else:
                present=False
                break
        return present

    def start_with_prefix(self,prefix):
        '''
        :param prefix:
        :return:All words that start with prefix
        '''
        words=[]
        if prefix is None:raise ValueError('Please put a not None prefix')
        # Determine end-of-prefix node
        top_node = self.root
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                # Prefix not in tree, go no further
                return words
        # Get words under prefix
        if top_node == self.root:
            queue = [node for key, node in top_node.children.items()]
        else:
            queue = [top_node]

        # Perform a BFS to get the words searched Lexicographically
        while queue:
            current_node = queue.pop()
            if current_node.data is not None:
                words.append(current_node.data)

            queue.extend([node for key, node in current_node.children.items()])

        return words

    def get_data(self, word):
        '''
        :param word:
        :return: get the data identified by a particular node
        '''
        if not self.has_word(word):
            raise ValueError('Word not found in the Trie')

        curr=self.root
        for letter in word:
            curr=curr.children[letter]
        return curr.data











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
        curr=self.root
        word_end=True

        for i in range(len(word)):
            if word[i] in curr.children:
                curr=curr.children[word[i]]# checking the letter is present or not
            else:
                # for ever new letter, if not present break create a new child node
                word_end=False
                break
        if not word_end:
            while i<len(word):
                curr.add_child(word[i])
                curr=curr.children[word[i]]
                i+=1
        curr.data=word

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
        top=self.root

        # Get to the end of the prefix
        for letter in prefix:
            if letter in top.children:
                top=top.children[letter]
            else:
                return words # preifix is not there at all

        #case '' and get the pointers to the start of the words
        queue = [node for key, node in top.children.items()] if top==self.root else [top]

        # Lexicographically search using BFS and get the words
        while queue:
            curr=queue.pop()
            print(curr.children)
            if curr.data is not None:
                words.append(curr.data)
            queue.append([node for key, node in curr.children.items()])

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

if __name__=='__main__':
    trie=Trie()

    # Defining the Test cases
    test1="You mean I can dodge the bullets"
    test2 = "This is your last chance. After this, there is no turning back. You take the blue pill - the story ends, you wake up in your bed and believe whatever you want to believe. You take the red pill - you stay in Wonderland and I show you how deep the rabbit-hole goes"
    test3 = "What is real? How do you define 'real'? If you're talking about what you can feel, what you can smell, what you can taste and see, then 'real' is simply electrical signals interpreted by your brain"
    tests = [test1]
    while tests:
        test=tests.pop(0)
        clean=re.sub(r"[,.;'\"\-_&$#@?!]+","",test)
        print(clean)
        for word in clean.split():
            #print(word)
            trie.insert(word)

        #check the functions here
        print(trie.has_word('bullets'))
        print(trie.start_with_prefix("t"))











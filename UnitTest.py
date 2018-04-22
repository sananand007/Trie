'''
Unit Tests for the trie Class
'''
from Trie import Trie, Trie_Node
import numpy as np
import re
from scrap_matrix import matrixQuotes

#TODO create a corpus and chose a word from the corpus to search for
#TODO Print the Trie structre

def tokentests(pick,trie):
    # Defining the Test cases
    testdefs={
    "test1": "Two of the toes in to the toss total trick tim has two bullets",
    "test2":"This is your last chance. After this, there is no turning back. You take the blue pill - the story ends, you wake up in your bed and believe whatever you want to believe. You take the red pill - you stay in Wonderland and I show you how deep the rabbit-hole goes",
    "test3": "What is real? How do you define 'real'? If you're talking about what you can feel, what you can smell, what you can taste and see, then 'real' is simply electrical signals interpreted by your brain",
    "test4": "To deny our own impulses is to deny the very thing that makes us human",
    "test5": "No, Neo. I'm trying to tell you that when you're ready, you won't have to",
    "test6": "I know you're out there. I can feel you now. I know that you're afraid... you're afraid of us. You're afraid of change. I don't know the future",
    "test7": "A world where anything is possible. Where we go from there is a choice I leave to you.",
    "test8": "I imagine that right now, you're feeling a bit like Alice. Hmm? Tumbling down the rabbit hole?",
    "test9": "That you are a slave, Neo. Like everyone else you were born into bondage. Into a prison that you cannot taste or see or touch. A prison for your mind",
    "test10": "Neo, sooner or later you're going to realize just as I did that there's a difference between knowing the path and walking the path"
    }
    test=testdefs["test"+str(pick)]
    clean=re.sub(r"[,.;'\"\-_&$#@?!]+","",test)
    print(clean)
    for word in clean.split():
        #print(word)
        trie.insert(word)
    #check the functions here
    print("is feel present, ", trie.has_word('feel'))
    print("prefix r, ", trie.start_with_prefix("r"))
    print("is see present, ", trie.has_word('see'))
    print("prefix s, ", trie.start_with_prefix("s"))



if __name__=='__main__':
    trie=Trie()
    pick = np.random.randint(0,9)
    tokentests(pick=pick, trie=trie)

#TODO Use the scrappy extension

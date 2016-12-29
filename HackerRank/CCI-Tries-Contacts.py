# Tries: Contacts
# https://www.hackerrank.com/challenges/ctci-contacts/copy-from/34680058
# We're going to make our own Contacts application! The application must perform two types of operations:
# 
# add name, where  is a string denoting a contact name. This must store  as a new contact in the application.
# find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.
# It is guaranteed that  and  contain lowercase English letters only.
# The input doesn't have any duplicate  for the  operation.

class Node(object):
    # use __slots__ to save memory 
    __slots__ = ['value', 'word_end', 'sub_words', 'children']
    def __init__(self, value):
        self.value = value
        self.word_end = False
        self.sub_words = 0 # number of word_end in subtree
        self.children = [None]*26 # only lowercase letters

class Contacts(object):
    def __init__(self):
        self.root = Node(None)
    
    def add(self, word):
        ''' Add a work to trie'''
        n = self.root
        n.sub_words += 1
        for c in word:
            index = ord(c) - ord('a')
            if not n.children[index]:
                nn = Node(c)
                n.children[index]=nn
            n = n.children[index]
            n.sub_words += 1
        n.word_end = True
        
    def find(self, pre):
        ''' count the number of words with prefix "pre" '''
        n = self.root
        for c in pre:
            index = ord(c) - ord('a')
            if not n.children[index]:
                return 0
            n = n.children[index]
        return n.sub_words
   
                
contacts = Contacts()
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == "add": 
        contacts.add(contact)
    elif op == "find":
        print contacts.find(contact)
    
    
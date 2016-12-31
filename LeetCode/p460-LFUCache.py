# 460. LFU Cache
# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and set.
# 
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?

# Design:
# we need 3 structures - 2 hash tables, 1 linked list
# self.data (dict): 
# 	- key = key
# 	- value = [value, reference of a node in self.forder]
# self.freq (dict):
# 	- key = frequency
# 	- value = reference of the last node with this frequency in self.forder
# self.forder (doubly linked list - FrequencyChain):
# 	- node: key, freq, next, prev


class LFUCache(object):

    def __init__(self, capacity):
        """
        
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.data = {}
        self.freq = {}
        self.forder = self.FrequencyChain()
        
    class Node(object):
		''' a node for the frequency linked list '''
		def __init__(self, key, freq):
			self.key = key
			self.freq = freq
			self.next = None
			self.prev = None       

#             
#     class Data(object):
#         ''' the value object of self.data '''
#         def __init__(self, val):
#             self.val = val
#             self.freq_node = None
            
    class FrequencyChain(object):
        ''' doubly linked list '''
        def __init__(self):
            self.head = None
            self.tail = None
            
        def insert(self, node1, node2):
            ''' insert node2 after node1 '''
            if node1:
                node2.next = node1.next
                node1.next = node2
            else: # node1==None means inserting at the beginning
                node2.next = self.head
                self.head = node2
            if node2.next:
                node2.next.prev = node2
            else:
                self.tail = node2
            node2.prev = node1
            
            
        def delete(self,node):
            ''' delete a node'''
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            
        def enqueue(self, node):
            ''' add a node to the tail '''
            if not self.head:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.node.prev = tail
                self.tail = node
                
        def dequeue(self):
            ''' delete the head '''
            self.delete(self.head)
            
        def __str__(self):
            s = []
            if self.head:
                cursor = self.head
                while cursor:
                    s.append((cursor.key,cursor.freq))
                    cursor = cursor.next
            return str(s)
            
            

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not self.data.has_key(key):
            return -1
        val = self.data[key][0]
        self.increase_freq(key)
        # print "after get: ", key, self.data, self.freq, self.forder
        return val

    def increase_freq(self, key):
        fnode = self.data[key][1]
        flag = True # need deletion 
        # delete the fnode from the old position
        if self.freq[fnode.freq] == fnode:
            flag = False
            if fnode.prev and fnode.prev.freq == fnode.freq:
                self.freq[fnode.freq] = fnode.prev
            else:
                del self.freq[fnode.freq]

        fnode.freq += 1
        
        # insert the fnode to the new position
        if self.freq.has_key(fnode.freq):
        	self.forder.delete(fnode)
        	self.forder.insert(self.freq[fnode.freq],fnode)
        elif flag:
            self.forder.delete(fnode)
            self.forder.insert(self.freq[fnode.freq-1],fnode)
        self.freq[fnode.freq] = fnode
        # if there are no freq+1 nodes and this node was the end, 
        # don't need to move this node

        	
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        # this key already exists
        if self.data.has_key(key):
            self.data[key][0] = value
            self.increase_freq(key)
            return 
        
        if self.capacity == 0: return
        if self.size == self.capacity:
            self.evict()
        
        # create the data object and add it to self.data
        fnode = self.Node(key,0)
        self.data[key] = [value, fnode]
                
        # update the frequency chain
        if self.freq.has_key(0):
            self.forder.insert(self.freq[0], fnode)
        else:
            self.forder.insert(None,fnode)
        self.freq[0] = fnode
        
        self.size += 1
        # print "after set: ", (key, value), self.data, self.freq, self.forder

    
    def evict(self):
        ''' delete the least frequently used data '''
        if (not self.forder.head.next or self.forder.head.freq 
				!= self.forder.head.next.freq):
            del self.freq[self.forder.head.freq]
        del self.data[self.forder.head.key]
        self.forder.dequeue()
        self.size -= 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
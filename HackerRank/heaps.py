''' implement a maxheap and a minheap
'''

class Heap(object):
    ''' Abstract class.
        Abstract methods: good_order()
    '''
    def __init__(self, arr=None):
    	if arr == None:
        	self.arr = []
        if self.arr:
            self.heapify()
    
    def is_empty(self):
    	return not self.arr
    
    def size(self):
		return len(self.arr)
		
    def add(self,value):
        self.arr.append(value)
        self.bubble_up(len(self.arr)-1)
        
    def delete(self,index):
        if index >= len(self.arr):
            raise IndexError("Index out of range!")
            return
        self.swap(index,-1)
        self.arr.pop()
        self.sink_down(index)
          
    def top(self):
        if not self.arr:
            raise "Heap is empty!"
        return self.arr[0]
    
    def poll(self):
        if not self.arr:
            raise "Heap is empty!"
        value = self.arr[0]
        self.delete(0)
        return value
    
    def heapify(self):
        for i in range((len(self.arr)-2)/2,-1,-1):
            self.sink_down(i)
        
    def bubble_up(self,index):
        pidx = self.parent_index(index)
        while (pidx >= 0 and 
               not self.good_order(pidx,index)):
            self.swap(pidx,index)
            index = pidx
            pidx = self.parent_index(index)
            
    def sink_down(self,index):
        while self.left_child_index(index) < len(self.arr):
            lidx = self.left_child_index(index)
            new_par = index
            if not self.good_order(index,lidx):
                new_par = lidx
            ridx = self.right_child_index(index)
            if ridx < len(self.arr):
                if not self.good_order(new_par,ridx):
                    new_par = ridx
            if index != new_par:
                self.swap(index,new_par)
                index = new_par
            else: break          
    
    def sort(self):
    	''' return a list with sorted elements sorting by heapsort'''
    	print "Warning: the heap is destroyed!"
    	ls = []
    	while not self.is_empty():
    		ls.append(self.poll())
    	return ls    	     
            
    def good_order(self, parent, child):
        '''Abstract method to check if parent and child are in good order'''
        raise NotImplementedError("good_order() is an abstract method!")
        
    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp
        
    def left_child_index(self,index):
        return 2*index + 1
    
    def right_child_index(self,index):
        return 2*index + 2
    
    def left_child_value(self,index):
        return arr[2*index + 1]
    
    def right_child_value(self,index):
        return arr[2*index + 2]
    
    def parent_index(self,index):
        return (index - 1)/2
    
    def parent_value(self,index):
        return arr[(index - 1)/2]
    
    def __str__(self):
    	return str(self.arr)

class MinHeap(Heap):
    def good_order(self, parent, child):
        return self.arr[parent]<=self.arr[child]
    
class MaxHeap(Heap):
    def good_order(self, parent, child):
        return self.arr[parent]>=self.arr[child]

if __name__ == "__main__":
	ls = [2,4,1,6,3,8,7,2,3]
	mh = MinHeap(ls)
	mh.add(-9)
	print mh
	print mh.sort()
	print mh

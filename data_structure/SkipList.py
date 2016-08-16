import random
from astropy.io.fits.convenience import update
class ListNode:
    def __init__(self,k,v,l):
        
        self.k = k 
        self.v = v
        self.l = l
        self.next_node = [None for i in range(l)]
       

    
    
class SkipList:
    def __init__(self,l = 1000):
        self.l = 1
        self.__len__ = 0
        self.head = ListNode(None,None,l)
     
    def __str__(self):
        re = ''
        x = self.head
        re += str(x.k) + ';'
        while x.next_node[0] is not None:
            x = x.next_node[0]
            re+= str(x.k) + ';'
        return re
    def __search__(self, k):
        levels = self.l
        update = [None]*levels
        x = self.head
         
        for i in reversed(range(levels)):
            while x.next_node[i] != None and x.next_node[i].k < k:
                x = x.next_node[i]
            update[i] = x
             
        return update
    
    def __getitem__(self, k):
        updates= self.__search__(k)
        
        if updates[0].k == k:
            return updates[0].v
        elif updates[0] is None or updates[0].next_node[0] is None or updates[0].next_node[0].k> k:
            raise Exception("item not found")
        else:
            return updates[0].next_node[0].v
            
            
    
    
    def __insert_node__(self,position,l,n_node):
        next_n = position.next_node[l]
        position.next_node[l] = n_node
        n_node.next_node[l] = next_n
        
    def __setitem__(self,k,v):
        self.__len__+=1
        ls = self.__len__ //2
        level = 0
        for l in range(ls,-1,-1):
            if random.random() < (1/(pow(2,l))):
                level = l+1
                break
        
         
        n_node = ListNode(k,v,level)
        updates = self.__search__(k)
        
        levels = min(self.l,level)
        
        [self.__insert_node__(updates[l], l, n_node) for l in range(levels)]

        if level > levels:
            for l in range(levels, level):
                self.head.next_node[l] = n_node
                
            
    


    

        
if __name__ == "__main__":
    test = SkipList()
    test[5] = 'e'
    for i in range(10):
        test[i] = 'a'
        print(test)
    for i in range(10):
        print(test[i])
    



       
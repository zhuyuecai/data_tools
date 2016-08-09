import random
class ListNode:
    def __init__(self,k,v,l):
        self.next_node = []
        self.k = k 
        self.v = v
        self.next_node = [None for i in range(l)]
        self.pre_node = [None for i in range(l)]

    
    
class SkipList:
    def __init__(self,k,v):
        self.next_node = []
        self.l=0
        self.__len__ = 0
        self.head = ListNode(k,v,1)
        self.next_node.append( self.head)
		
		
		
    def __helper(self,current,k,l):
        #print (current.next_node)
        #print (l)
        if current.next_node[l] is None:
            return current
        elif current.next_node[l].k > k:
            return current
        else:
            return self.__helper(current.next_node[l],k,l)         
    
    def __search_by_level(self, k, l):
        current = self.__helper(self.next_node[l],k,l)
 
        return current
        
    
    def __getitem__(self, k):
            
        l_h = len(self.next_node)
        
        current = self.next_node[l_h-1]
        while(l_h>=0):
            l_h-=1
            if current.k == k: 
                return current.v
            elif current.k > k:
                current = self.next_node[l_h-1]
            else:
                current = self.__helper(current,k,l_h)
            
        raise Exception("item not found")
            
            
    
    
    
    
    def __setitem__(self,k,v):
        self.__len__+=1
        ls = self.__len__ //2
        if ls > self.l : self.l = ls
        level = 0
  
        for l in range(self.l,-1,-1):
            if random.random() < (1/(pow(2,l))):
                level = l
                break
   
        n_node = ListNode(k,v,level+1)
        for l in range(level+1):
            self.__setbylevel___(l,n_node)
        
    
    def __setbylevel___(self,l,n_node):
        if (l+1) > len(self.next_node):
            self.next_node.append(n_node)
        else:
            
            if self.next_node[l].k > n_node.k:
                n_node.next_node[l] = self.next_node[l]
                self.next_node[l].pre_node[l] = n_node
                self.next_node[l] = n_node 				
            else:
                current = self.__search_by_level(n_node.k, l)
            
                if current.k == n_node.k:
                    current.v = n_node.v
                else:
                    
                    next = current.next_node[l]
                    n_node.pre_node[l] = current
                    n_node.next_node[l] = next
                    if next is not None:
                        next.pre_node[l]= n_node
                    current.next_node[l] = n_node
    

    

    

        
if __name__ == "__main__":
    test = SkipList(5,'e')
    print(test[5])
    for i in range(10):
        test[i] = 'a'
    for i in range(10):
        print (test[i])



       
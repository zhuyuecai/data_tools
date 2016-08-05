#Hash table
import numpy as np

class HashTable:
    def __init__(self,k_dt, v_dt, size = 1000):
            self.__size = size
            self.__val = np.zeros(size,dtype = v_dt)
            self.__key = np.zeros(size,dtype = k_dt)
    
    def __hash_key(self,k,size):
        return hash(k)%size

    def insert(self,k_v_pair):
        p = self.__hash_key(k_v_pair[0],self.__size)
        while(not self.__key[p] and p<self.__size-1):
            p+=1
        self.__val[p] = k_v_pair[1]
        self.__key[p] = k_v_pair[0]
    
    def __find_k(self, k):
        p = self.__hash_key(k,self.__size)
        while( not self.__key[p]== k ):
            if p < self.__size:
                p+=1
            else:
                p = -1
                break
        return p
 
    def delete(self,k):
        p = self.__find(k)
        if p >=0:
            self.__key[p] = 0
            self.__val[p] = null

    def search_by_key(self, k):
        p =  self. __find_k(k)
        if p > -1:
            return self.__val[p]
        else:
            return null
   


if __name__ == "__main__" :
    test_table = HashTable("i8", "a25")
    test_table.insert([3,"gerg"])
    a= test_table.search_by_key(3)
    print a
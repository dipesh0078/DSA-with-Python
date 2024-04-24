#dictionary implement hash table
class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]
    def get_hash(self,key):
     h=0
     for char in key:
        h+=ord(char)
     return h%100  #100 size of list
    
    def add(self,key,val):
       h=self.get_hash(key)
       self.arr[h]=val
    
    def get(self,key):
       h=self.get_hash(key)
       return self.arr[h]
    def delete(self, key):
       h=self.get_hash(key)
       self.arr[h]=None
       


t=HashTable()
t.add('march 6',130)
t.add('march 1', 400)
t.add('march 3', 3434)
print(t.get('march 6'))
t.delete('march 6')
print(t.get('march 6'))

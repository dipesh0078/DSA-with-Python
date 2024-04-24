class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.prev=prev
        self.next=next

class DoublyLinkendList:
    def __init__(self):
        self.head=None
    
    def print(self):
        itr=self.head
        dll=''
        while itr.next:
            dll=dll+ itr.data + '-->'
            itr=itr.next
        print(dll)
    
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count
    
    def insert_at_begining(self,data):
        node=Node(data,self.head,None)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        node=Node(data,None,itr.next)
        itr.next=node
    
    def insert_at(self,index,data):
       if index<0 or index>self.get_length():
           raise Exception("Invalid Index")
       if index==0:
           node=Node(data,self.head,None)
           self.head=node
           return
       itr=self.head
       count=0
       while itr:
           if count==index-1:
               node=Node(data, itr.next, itr)
               if itr.next:
                  itr.next.prev=node
               itr.next=node
               break
           count+=1
           itr=itr.next

    
    def remove_at(self,index):
         if index<0 or index>=self.get_length():
           raise Exception("Invalid Index")
         if index==0:
             self.head=self.head.next
             self.head.prev=None
             return
         
         count=0
         itr=self.head
         while itr:
             if count==index:
                 itr.next=itr.next.next
                 itr.next.prev=itr.prev
             itr=itr.next
             count+=1

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self,data_after,data):
        itr=self.head
        while itr:
            if data_after==itr.data:
                node=Node(data,itr.next,itr)
                if itr.next:
                    itr.next.prev=node
                itr.next=node
                break
            itr=itr.next
    def remove_by_value(self, data):
        itr=self.head
        while itr:
            if itr.data==data:
                itr.prev.next=itr.next
                itr.next.prev=itr.prev
                break
            itr=itr.next

if __name__ == '__main__':
    ll = DoublyLinkendList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    
    ll.insert_at_end("figs")
    ll.print()
    ll.insert_at(0,"jackfruit")
    ll.print()
    ll.insert_at(6,"dates")
    ll.print()
    ll.insert_at(2,"kiwi")
    ll.print()
    ll.remove_by_value('kiwi')
    ll.print()
    ll.insert_after_value('mango','Dragon')
    ll.print()
        



                 
         

           
           
         

        
        







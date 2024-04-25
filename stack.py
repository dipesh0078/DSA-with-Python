#implementing stack using deque
from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
       return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    def is_empty(self):
       if len(self.container)==0:
           return True
       else:
           return False
    
    def size(self):
        return len(self.container)


strin='We will conquere COVID-19'

def reverse(str):
    reverse_stack=Stack()
    count=len(str)
    reverse=''
    for i in str:
        reverse_stack.push(i)
    while count>0:
        reverse +=reverse_stack.pop()
        count-=1
    return reverse
    



'''Write a function in 
python that checks if paranthesis in the string are
 balanced or not. 
 Possible parantheses are "{}',"()" or "[]".
Use Stack class from the tutorial.'''

def is_balanced(s):
    stack = Stack()
    for char in s:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if (char == '}' and top_char != '{') or \
               (char == ')' and top_char != '(') or \
               (char == ']' and top_char != '['):
                return False
    return stack.is_empty()
          

print(is_balanced("({a+b})") )


print(reverse(strin))

class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,char):
        for i in range(len(char)):
            self.stack.append(char[i])      #append the stack 
            
    def pop(self):
        if len(self.stack)<=0:
            exit(0)
        self.stack.pop()                    #pop the item
        
    def isEmpty(self):
        return len(self.stack)<=0
        
    def reverse(self,word):
        word=word[::-1]                      #reverse the given string
        return word
        
    def show(self):
        return self.stack
        
s=Stack()
word=input()
s.push(word)
y=s.show()
z=''.join(y)
print("YES" if z==s.reverse(word) else "NO")

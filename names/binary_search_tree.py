import sys

class BinarySearchTree: 
    def __init__(self,value):
          self.value = value
          self.left = None
          self.right = None

# insert the given value into the tree

    def insert(self,value):
        if self.value is None:
                self.value = BinarySearchTree(value)
        else:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
            else:  
                if self.right:     
                    self.right.insert(value)
                if self.right:
                    self.right.insert(value) 
                else:
                    self.right = BinarySearchTree(value)    
# returns true if the tree contains the value
# False if it does not 
    def contains(self, target):
        if target == self.value:
            return True
        else:    
            if target[0] < self.value[0] and self.left[0]:
                 return self.left.contains(target)
            else: 
                if target[0] > self.value[0] and self.right[0]:
                    return self.right.contains(target)
            return False        

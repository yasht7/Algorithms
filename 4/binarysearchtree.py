class TreeNode(object):

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    # custom helper functions
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self ,key, value, lc, rc):
        self.key = key
        self.val = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.height = 0

    def length(self):
        return self.height

    def __len__(self):
        return self.height

    def put(self, key, val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.height += 1

    def _put(self, key, val, x):
        if key < x.key:
            if x.hasLeftChild():
                self._put(key, val, x.leftChild)
            else:
                x.leftChild = TreeNode(key, val, parent=x)
        else:
            if x.hasRightChild():
                    self._put(key, val, x.rightChild)
            else:
                    x.rightChild = TreeNode(key, val, parent=x)

    def __setitem__(self, k, v):
       self.put(k, v)

    def get(self, key):
       if self.root:
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None
       else:
            return None

    def _get(self, key, x):
       if not x:
            return None
       elif x.key == key:
            return x
       elif key < x.key:
            return self._get(key, x.leftChild)
       else:
            return self._get(key, x.rightChild)

    def __getitem__(self, key):
       return self.get(key)

    def __contains__(self, key):
       if self._get(key, self.root):
           return True
       else:
           return False

    def delete(self, key):
        if self.height > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.height -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.height == 1 and self.root.key == key:
            self.root = None
            self.height -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
           else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current


if __name__ == "__main__":
    mytree = BinarySearchTree()
    mytree[3]="three"
    mytree[4]="four"
    mytree[6]="six"
    mytree[2]="two"
    print(mytree[6])
    print(mytree[2])

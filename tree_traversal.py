class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"

#inorder , pre oder, post order traversal

#tree -node, left, right

class binary_tree():
    def __init__(self,node):
        self.node=node
        print("type node", type(self.node))
        print("type node", type(node))
        self.left=None #" It is a object data type"
        print( "type left ", type(self.left))
        #print("ledt 0000", self.left)
        self.right=None #" It is a object data type"
        print("type right", type(self.left))
        print ("Node data, self node =",node, self.node)

    def insert_in_tree(self,data1):
        if self.node :
            print("your_input_data1, self node",data1,self.node )
            if data1 < self.node:
                if self.left == None:
                    print("left_side data1, self node ",data1, self.node)
                    self.left = binary_tree(data1)
                else:
                    print("ledt,,,,,,,,,, 0000", self.left)
                    print("left_else side data1, self node ", data1, self.node)
                    self.left.insert_in_tree(data1)
                    print("ledt",self.left)
            if data1 > self.node:
                if self.right == None:
                    print("right_side data1, self node ", data1, self.node)
                    self.right = binary_tree(data1)
                else:
                    print("right else_side data1, self node ", data1, self.node)
                    self.right.insert_in_tree(data1)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print("selfnode",self.node)
        if self.right:
            self.right.print_tree()

b_root=binary_tree(12)
b_root.insert_in_tree(6)
b_root.insert_in_tree(14)
b_root.insert_in_tree(3)
b_root.insert_in_tree(30)
b_root.insert_in_tree(20)
b_root.insert_in_tree(10)
b_root.insert_in_tree(44)

b_root.print_tree()
type(5)
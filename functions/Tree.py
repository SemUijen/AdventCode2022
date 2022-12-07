
# Classes
class Node:
    def __init__(self, ID, level, Parent, Name, Type, Size):
        self.children = []
        self.ID = ID
        self.Level = level
        self.Parent = Parent

        self.Name = Name
        self.Type = Type
        self.Size = Size

    def Node_tostring(self):
        String = ("Node ID: " + str(self.ID),
                  "Node Level: " + str(self.Level),
                  "Node Name: " + str(self.Name),
                  "Node Type: " + str(self.Type),
                  "Node Size: " + str(self.Size))
        String = str(String)
        return String

    def add_Node(self,Name, Type, Size):
        level = self.Level + 1
        ID = self.ID + (len(self.children) + 1) / 100 ** self.Level
        self.children.append(
            Node(ID, level, self, Name, Type, Size))

        return ID


class Tree:
    def __init__(self, root):
        self.root = root

    def getRoot(self):
        return self.root

    def find(self, val):
        if (self.root != None):
            return self._find(val, self.root)
        else:
            return "empty tree"

    def _find(self, val, node):

        if (val == node.ID):
            return node

        # if node has no children then ID is not in the tree
        if len(node.children) == 0:
            return print("error", val, "not found")
        # if node only has one child below find method doesnt work
        if len(node.children) == 1:
            return self._find(val, node.children[0])

        # loop through children of a node. val must be between IDs of two children(this is the way the tree is setup)
        for i in range(len(node.children) - 1):
            if val >= node.children[i].ID and val < node.children[i + 1].ID:
                return self._find(val, node.children[i])
        return node.children[len(node.children) - 1]

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):

        if self.root is not None:
            print(self.root.Node_tostring())
            self._printTree(self.root)

    def _printTree(self, Node):
        # add spaces for increase in Tree level
        Spaces = ' ' * 2 * (Node.Level + 1)
        if Node.children != []:
            for child in Node.children:
                print(Spaces, child.Node_tostring())
                self._printTree(child)

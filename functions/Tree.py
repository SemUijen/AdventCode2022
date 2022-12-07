# Classes
class Node:
    def __init__(self, ID, level, Parent, Name, Type):
        self.children = []
        self.ID = ID
        self.Level = level
        self.Parent = Parent

        self.Name = Name
        self.Type = Type
        self.Size = 0

    def Node_tostring(self):
        String = ('- ' + str(self.Name) + ' ' + str(self.Type) + ' ' + 'size: ' + str(self.Size) + ' ' + str(self.ID))
        String = str(String)
        return String

    def add_Node(self, Name, Type):
        level = self.Level + 1
        ID = self.ID + (len(self.children) + 1) / 100 ** self.Level
        self.children.append(
            Node(ID, level, self, Name, Type))

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
        if val == node.ID:
            return node

        # if node has no children then ID is not in the tree
        if len(node.children) == 0:
            return print("error", val, "not found")

        # if node only has one child below find method doesnt work
        if len(node.children) == 1:
            return self._find(val, node.children[0])

        # loop through children of a node. val must be between IDs of two children(this is the way the tree is setup)
        for i in range(len(node.children) - 1):
            if node.children[i].ID <= val < node.children[i + 1].ID:
                return self._find(val, node.children[i])

        return self._find(val, node.children[len(node.children) - 1])

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

    def find_largeDir(self):
        score = 0
        if self.root is not None:
            if self.root.Size <= 100000:
                score += self.root.Size

            score = self._find_largeDir(self.root, score)

        print(score)
        return score

    def _find_largeDir(self, node, score):

        if node.children != []:
            for child in node.children:

                if child.Type == 'dir' and child.Size <= 100000:
                    score += child.Size
                    print(child.Name)
                    print(child.Size)
                    print(score)
                score = self._find_largeDir(child, score)


        return score

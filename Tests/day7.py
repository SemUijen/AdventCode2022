lines = open('../data/day7_input.txt', 'r')
from functions.Tree import Tree, Node

#directory names are not unique!

def Create_tree():
    dir_tree_dict = {}
    dir_tree = Tree(Node(0, 0, None, "/", 'dir'))

    current_nodeID = 0
    for line in lines:
        if 'cd' == line.split()[1]:
            if '/' == line.split()[2]:
                current_nodeID = dir_tree.getRoot().ID
                current_node = dir_tree.find(current_nodeID)

            if '..' == line.split()[2]:
                size = current_node.Size
                current_nodeID = current_node.Parent.ID
                current_node = dir_tree.find(current_nodeID)
                current_node.Size += size

            elif not '/' == line.split()[2]:
                current_nodeID = dir_tree_dict[line.split()[2]]
                current_node = dir_tree.find(current_nodeID)

        else:
            if 'dir' in line:
                current_node_id = current_node.add_Node(line.split()[1], 'dir')
                dir_tree_dict[line.split()[1]] = current_node_id

            elif '$ ls' != line.replace('\n', ''):

                current_nodeID = current_node.add_Node(line.split()[1], 'file')
                dir_tree_dict[line.split()[1]] = current_nodeID

                dir_tree.find(current_nodeID).Size += int(line.split()[0])
                current_node.Size += int(line.split()[0])

    #print(dir_tree_dict)
    #dir_tree.printTree()
    return dir_tree


def day7_part1():
    dir_tree = Create_tree()
    dir_tree.printTree()
    score = dir_tree.find_largeDir()

    return score

day7_part1()
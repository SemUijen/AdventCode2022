lines = open('../data/day7_input.txt', 'r')
from functions.Tree import Tree, Node

# there are duplicates in filename

def Create_tree():
    dir_tree_dict = {}
    dir_tree = Tree(Node(0, 0, None, "/", 'dir'))

    current_nodeID = 0
    for line in lines:
        try:
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
                    #current_nodeID = dir_tree_dict[line.split()[2]]

                    current_nodeID = current_node.add_Node(line.split()[2], 'dir')
                    current_node = dir_tree.find(current_nodeID)

            else:
                #if 'dir' in line:
                    #current_node_id = current_node.add_Node(line.split()[1], 'dir')
                    #dir_tree_dict[line.split()[1]] = current_node_id

                if '$ ls' != line.replace('\n', '') and 'dir' not in line:

                    current_nodeID = current_node.add_Node(line.split()[1], 'file')
                    dir_tree_dict[line.split()[1]] = current_nodeID
                    dir_tree.find(current_nodeID).Size += int(line.split()[0])
                    current_node.Size += int(line.split()[0])

        except Exception as ex:
            dir_tree.printTree()
            break

    for i in range(current_node.Level):
        size = current_node.Size

        current_nodeID = current_node.Parent.ID
        current_node = dir_tree.find(current_nodeID)
        current_node.Size += size

    return dir_tree


def day7_part1():
    dir_tree = Create_tree()
    #dir_tree.printTree()
    best_dir_size = dir_tree.find_largeDir()

    return best_dir_size

def day7_part2():
    dir_tree = Create_tree()
    #dir_tree.printTree()
    min_to_remove = 30000000 - (70000000 - dir_tree.getRoot().Size)
    score = dir_tree.find_bestDir(min_to_remove)

    return score


print(day7_part2())